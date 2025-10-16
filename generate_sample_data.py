import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
from faker import Faker
import os


class EcommerceDataGenerator:
    def __init__(self, seed=42):
        self.fake = Faker('zh_CN')
        np.random.seed(seed)
        random.seed(seed)
        self.fake.seed_instance(seed)

        # 创建数据目录
        os.makedirs('data/raw', exist_ok=True)
        os.makedirs('data/processed', exist_ok=True)
        os.makedirs('data/features', exist_ok=True)
        os.makedirs('data/output', exist_ok=True)

    def generate_users_data(self, n_users=10000):
        """生成用户数据"""
        print("生成用户数据...")

        users = []
        for i in range(n_users):
            user_id = f"U{10000 + i:05d}"
            register_date = self.fake.date_between(start_date='-2y', end_date='today')

            user = {
                'user_id': user_id,
                'register_date': register_date,
                'region': self.fake.province(),
                'age': random.randint(18, 65),
                'gender': random.choice(['男', '女']),
                'registration_channel': random.choice(['网站', 'APP', '微信小程序', '线下推广']),
                'last_login_date': self.fake.date_between(start_date=register_date, end_date='today')
            }
            users.append(user)

        users_df = pd.DataFrame(users)
        users_df.to_csv('data/raw/users.csv', index=False, encoding='utf-8')
        return users_df

    def generate_products_data(self, n_products=500):
        """生成产品数据"""
        print("生成产品数据...")

        categories = {
            '电子产品': ['手机', '笔记本电脑', '平板电脑', '智能手表', '耳机'],
            '服装': ['T恤', '衬衫', '裤子', '外套', '裙子'],
            '家居': ['床上用品', '厨房用具', '装饰品', '家具', '灯具'],
            '美妆': ['护肤品', '化妆品', '香水', '美发产品'],
            '食品': ['零食', '饮料', '生鲜', '粮油调味']
        }

        products = []
        for i in range(n_products):
            product_id = f"P{1000 + i:04d}"
            category = random.choice(list(categories.keys()))
            subcategory = random.choice(categories[category])

            # 基础价格
            base_price = round(random.uniform(50, 2000), 2)
            # 成本通常是价格的60%-80%
            cost = round(base_price * random.uniform(0.6, 0.8), 2)

            product = {
                'product_id': product_id,
                'product_name': f"{subcategory}{i + 1}",
                'category': category,
                'subcategory': subcategory,
                'price': base_price,
                'cost': cost,
                'stock_quantity': random.randint(0, 1000),
                'created_date': self.fake.date_between(start_date='-3y', end_date='-6m')
            }
            products.append(product)

        products_df = pd.DataFrame(products)
        products_df.to_csv('data/raw/products.csv', index=False, encoding='utf-8')
        return products_df

    def generate_orders_data(self, n_orders=50000, users_df=None, products_df=None):
        """生成订单数据"""
        print("生成订单数据...")

        orders = []
        order_items = []

        user_ids = users_df['user_id'].tolist()
        product_ids = products_df['product_id'].tolist()
        product_prices = products_df.set_index('product_id')['price'].to_dict()

        order_id_counter = 100000

        for i in range(n_orders):
            order_id = f"O{order_id_counter + i}"
            user_id = random.choice(user_ids)

            # 订单日期（最近2年）
            order_date = self.fake.date_time_between(start_date='-2y', end_date='now')

            # 每个订单1-5个商品
            n_items = random.randint(1, 5)
            order_items_list = random.sample(product_ids, n_items)

            total_amount = 0
            items_data = []

            for product_id in order_items_list:
                quantity = random.randint(1, 3)
                price = product_prices[product_id]
                item_total = price * quantity
                total_amount += item_total

                items_data.append({
                    'order_id': order_id,
                    'product_id': product_id,
                    'quantity': quantity,
                    'unit_price': price,
                    'item_total': item_total
                })

            # 添加一些随机优惠
            discount = round(total_amount * random.uniform(0, 0.3), 2)
            final_amount = total_amount - discount

            order = {
                'order_id': order_id,
                'user_id': user_id,
                'order_date': order_date,
                'total_amount': total_amount,
                'discount_amount': discount,
                'final_amount': final_amount,
                'shipping_fee': random.choice([0, 5, 10, 15]),
                'payment_method': random.choice(['支付宝', '微信支付', '信用卡', '银行卡']),
                'order_status': random.choices(
                    ['已完成', '已发货', '待发货', '已取消'],
                    weights=[0.7, 0.15, 0.1, 0.05]
                )[0]
            }

            orders.append(order)
            order_items.extend(items_data)

        orders_df = pd.DataFrame(orders)
        order_items_df = pd.DataFrame(order_items)

        orders_df.to_csv('data/raw/orders.csv', index=False, encoding='utf-8')
        order_items_df.to_csv('data/raw/order_items.csv', index=False, encoding='utf-8')

        return orders_df, order_items_df

    def generate_user_behavior_data(self, n_records=100000, users_df=None, products_df=None):
        """生成用户行为数据"""
        print("生成用户行为数据...")

        behaviors = []
        user_ids = users_df['user_id'].tolist()
        product_ids = products_df['product_id'].tolist()

        behavior_types = ['view', 'cart', 'purchase', 'wishlist']

        for i in range(n_records):
            user_id = random.choice(user_ids)
            product_id = random.choice(product_ids)
            behavior_type = random.choices(
                behavior_types,
                weights=[0.6, 0.2, 0.15, 0.05]
            )[0]

            # 行为时间（最近1年）
            behavior_time = self.fake.date_time_between(start_date='-1y', end_date='now')

            behavior = {
                'user_id': user_id,
                'product_id': product_id,
                'behavior_type': behavior_type,
                'behavior_time': behavior_time,
                'duration_seconds': random.randint(10, 600) if behavior_type == 'view' else 0,
                'session_id': f"SESS{random.randint(10000, 99999)}"
            }

            behaviors.append(behavior)

        behavior_df = pd.DataFrame(behaviors)
        behavior_df.to_csv('data/raw/user_behavior.csv', index=False, encoding='utf-8')
        return behavior_df

    def generate_data_dictionary(self):
        """生成数据字典文档"""
        print("生成数据字典...")

        data_dict = {
            'users.csv': {
                'user_id': '用户ID，唯一标识符',
                'register_date': '注册日期',
                'region': '所在地区',
                'age': '年龄',
                'gender': '性别',
                'registration_channel': '注册渠道',
                'last_login_date': '最后登录日期'
            },
            'products.csv': {
                'product_id': '产品ID，唯一标识符',
                'product_name': '产品名称',
                'category': '产品类别',
                'subcategory': '产品子类别',
                'price': '产品价格',
                'cost': '产品成本',
                'stock_quantity': '库存数量',
                'created_date': '产品创建日期'
            },
            'orders.csv': {
                'order_id': '订单ID，唯一标识符',
                'user_id': '用户ID',
                'order_date': '订单日期',
                'total_amount': '订单总金额',
                'discount_amount': '优惠金额',
                'final_amount': '实付金额',
                'shipping_fee': '运费',
                'payment_method': '支付方式',
                'order_status': '订单状态'
            },
            'order_items.csv': {
                'order_id': '订单ID',
                'product_id': '产品ID',
                'quantity': '购买数量',
                'unit_price': '单价',
                'item_total': '商品总价'
            },
            'user_behavior.csv': {
                'user_id': '用户ID',
                'product_id': '产品ID',
                'behavior_type': '行为类型（view-浏览，cart-加购，purchase-购买，wishlist-收藏）',
                'behavior_time': '行为时间',
                'duration_seconds': '停留时长（秒）',
                'session_id': '会话ID'
            }
        }

        with open('data/raw/data_dictionary.md', 'w', encoding='utf-8') as f:
            f.write("# 数据字典说明\n\n")
            for file_name, columns in data_dict.items():
                f.write(f"## {file_name}\n\n")
                f.write("| 字段名 | 说明 |\n")
                f.write("|-------|------|\n")
                for col_name, description in columns.items():
                    f.write(f"| {col_name} | {description} |\n")
                f.write("\n")

    def generate_sample_data(self):
        """生成所有样本数据"""
        print("开始生成电商样本数据...")

        # 生成用户数据
        users_df = self.generate_users_data(10000)

        # 生成产品数据
        products_df = self.generate_products_data(500)

        # 生成订单数据
        orders_df, order_items_df = self.generate_orders_data(50000, users_df, products_df)

        # 生成用户行为数据
        behavior_df = self.generate_user_behavior_data(100000, users_df, products_df)

        # 生成数据字典
        self.generate_data_dictionary()

        print("\n数据生成完成！")
        print(f"用户数据: {len(users_df)} 条")
        print(f"产品数据: {len(products_df)} 条")
        print(f"订单数据: {len(orders_df)} 条")
        print(f"订单商品数据: {len(order_items_df)} 条")
        print(f"用户行为数据: {len(behavior_df)} 条")

        return {
            'users': users_df,
            'products': products_df,
            'orders': orders_df,
            'order_items': order_items_df,
            'behavior': behavior_df
        }


def main():
    """主函数"""
    print("电商数据分析项目 - 样本数据生成器")
    print("=" * 50)

    # 检查是否需要安装faker
    try:
        import faker
    except ImportError:
        print("检测到未安装 faker 库，正在安装...")
        import subprocess
        subprocess.check_call(['pip', 'install', 'faker'])
        print("faker 库安装完成！")

    # 生成数据
    generator = EcommerceDataGenerator()
    data = generator.generate_sample_data()

    print("\n生成的文件保存在 data/raw/ 目录：")
    print("✅ users.csv - 用户基本信息")
    print("✅ products.csv - 产品信息")
    print("✅ orders.csv - 订单交易数据")
    print("✅ order_items.csv - 订单商品明细")
    print("✅ user_behavior.csv - 用户行为日志")
    print("✅ data_dictionary.md - 数据字典说明")

    print("\n数据生成完成！现在可以运行分析项目了。")


if __name__ == "__main__":
    main()