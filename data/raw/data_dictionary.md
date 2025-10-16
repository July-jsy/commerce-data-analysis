# 数据字典说明

## users.csv

| 字段名 | 说明 |
|-------|------|
| user_id | 用户ID，唯一标识符 |
| register_date | 注册日期 |
| region | 所在地区 |
| age | 年龄 |
| gender | 性别 |
| registration_channel | 注册渠道 |
| last_login_date | 最后登录日期 |

## products.csv

| 字段名 | 说明 |
|-------|------|
| product_id | 产品ID，唯一标识符 |
| product_name | 产品名称 |
| category | 产品类别 |
| subcategory | 产品子类别 |
| price | 产品价格 |
| cost | 产品成本 |
| stock_quantity | 库存数量 |
| created_date | 产品创建日期 |

## orders.csv

| 字段名 | 说明 |
|-------|------|
| order_id | 订单ID，唯一标识符 |
| user_id | 用户ID |
| order_date | 订单日期 |
| total_amount | 订单总金额 |
| discount_amount | 优惠金额 |
| final_amount | 实付金额 |
| shipping_fee | 运费 |
| payment_method | 支付方式 |
| order_status | 订单状态 |

## order_items.csv

| 字段名 | 说明 |
|-------|------|
| order_id | 订单ID |
| product_id | 产品ID |
| quantity | 购买数量 |
| unit_price | 单价 |
| item_total | 商品总价 |

## user_behavior.csv

| 字段名 | 说明 |
|-------|------|
| user_id | 用户ID |
| product_id | 产品ID |
| behavior_type | 行为类型（view-浏览，cart-加购，purchase-购买，wishlist-收藏） |
| behavior_time | 行为时间 |
| duration_seconds | 停留时长（秒） |
| session_id | 会话ID |

