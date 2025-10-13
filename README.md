# 目录结构

📦 ecommerce-data-analysis/
├── 📁 data/                               # 数据目录
│   ├── 📁 raw/                           # 原始数据（只读）
│   │   ├── 📄 users.csv                  # 用户基本信息
│   │   ├── 📄 orders.csv                 # 订单交易数据
│   │   ├── 📄 products.csv               # 产品信息表
│   │   ├── 📄 user_behavior.csv          # 用户行为日志
│   │   └── 📄 data_dictionary.md         # 数据字典说明
│   ├── 📁 processed/                     # 清洗后数据
│   │   ├── 📄 cleaned_users.csv
│   │   ├── 📄 cleaned_orders.csv
│   │   ├── 📄 cleaned_products.csv
│   │   └── 📄 data_quality_report.html
│   ├── 📁 features/                      # 特征工程数据
│   │   ├── 📄 user_features.csv
│   │   ├── 📄 product_features.csv
│   │   ├── 📄 temporal_features.csv
│   │   └── 📄 feature_correlation_matrix.csv
│   └── 📁 output/                        # 分析输出结果
│       ├── 📁 reports/                   # 分析报告
│       │   ├── 📄 executive_summary.pdf
│       │   ├── 📄 detailed_analysis.pdf
│       │   ├── 📄 business_recommendations.pdf
│       │   └── 📄 technical_report.md
│       ├── 📁 visualizations/            # 可视化图表
│       │   ├── 📁 exploratory/           # 探索性图表
│       │   ├── 📁 user_analysis/         # 用户分析图表
│       │   ├── 📁 sales_analysis/        # 销售分析图表
│       │   └── 📁 dashboards/            # 仪表板图表
│       ├── 📁 models/                    # 训练好的模型
│       │   ├── 📄 user_clustering.pkl
│       │   ├── 📄 churn_prediction.pkl
│       │   └── 📄 sales_forecast.pkl
│       └── 📁 insights/                  # 关键洞察
│           ├── 📄 key_metrics.json
│           ├── 📄 user_segments.json
│           └── 📄 product_analysis.json
├── 📁 src/                               # 源代码目录
│   ├── 📁 data/                          # 数据处理模块
│   │   ├── 📄 __init__.py
│   │   ├── 📄 data_loader.py             # 数据加载器
│   │   ├── 📄 data_cleaner.py            # 数据清洗器
│   │   ├── 📄 data_validator.py          # 数据验证器
│   │   ├── 📄 data_transformer.py        # 数据转换器
│   │   └── 📄 feature_engineer.py        # 特征工程
│   ├── 📁 analysis/                      # 分析模块
│   │   ├── 📄 __init__.py
│   │   ├── 📄 exploratory_analysis.py    # 探索性分析
│   │   ├── 📄 user_analysis.py           # 用户行为分析
│   │   ├── 📄 sales_analysis.py          # 销售趋势分析
│   │   ├── 📄 product_analysis.py        # 产品表现分析
│   │   ├── 📄 statistical_analysis.py    # 统计分析
│   │   └── 📄 cohort_analysis.py         # 同期群分析
│   ├── 📁 modeling/                      # 建模模块
│   │   ├── 📄 __init__.py
│   │   ├── 📄 clustering.py              # 聚类分析
│   │   ├── 📄 classification.py          # 分类模型
│   │   ├── 📄 regression.py              # 回归模型
│   │   ├── 📄 time_series.py             # 时间序列
│   │   └── 📄 model_evaluation.py        # 模型评估
│   ├── 📁 visualization/                 # 可视化模块
│   │   ├── 📄 __init__.py
│   │   ├── 📄 exploratory_charts.py      # 探索性图表
│   │   ├── 📄 business_charts.py         # 业务图表
│   │   ├── 📄 dashboard_components.py    # 仪表板组件
│   │   ├── 📄 report_templates.py        # 报告模板
│   │   └── 📄 style_config.py            # 样式配置
│   ├── 📁 utils/                         # 工具模块
│   │   ├── 📄 __init__.py
│   │   ├── 📄 config_loader.py           # 配置加载器
│   │   ├── 📄 logger.py                  # 日志配置
│   │   ├── 📄 helpers.py                 # 辅助函数
│   │   ├── 📄 constants.py               # 常量定义
│   │   └── 📄 decorators.py              # 装饰器
│   └── 📁 scripts/                       # 执行脚本目录
│       ├── 📄 run_data_pipeline.py       # 数据管道脚本
│       ├── 📄 run_user_analysis.py       # 用户分析脚本
│       ├── 📄 run_sales_analysis.py      # 销售分析脚本
│       ├── 📄 run_product_analysis.py    # 产品分析脚本
│       ├── 📄 run_full_analysis.py       # 完整分析脚本
│       └── 📄 generate_reports.py        # 报告生成脚本
├── 📁 config/                            # 配置文件目录
│   ├── 📄 analysis_config.yaml           # 分析参数配置
│   ├── 📄 modeling_config.yaml           # 建模参数配置
│   ├── 📄 visualization_config.yaml      # 可视化配置
│   ├── 📄 data_config.yaml               # 数据配置
│   └── 📄 paths_config.yaml              # 路径配置
├── 📁 tests/                             # 测试目录
│   ├── 📁 test_data/                     # 测试数据
│   ├── 📁 test_analysis/                 # 分析测试
│   ├── 📁 test_models/                   # 模型测试
│   ├── 📁 test_visualization/            # 可视化测试
│   ├── 📄 conftest.py                    # pytest配置
│   └── 📄 test_main.py                   # 主流程测试
├── 📁 docs/                              # 项目文档
│   ├── 📄 project_specification.md       # 项目规格说明
│   ├── 📄 data_dictionary.md             # 详细数据字典
│   ├── 📄 analysis_methodology.md        # 分析方法论
│   ├── 📄 user_guide.md                  # 用户指南
│   ├── 📄 api_reference.md               # API参考
│   └── 📄 deployment_guide.md            # 部署指南
├── 📁 logs/                              # 日志目录
│   ├── 📄 data_processing.log            # 数据处理日志
│   ├── 📄 analysis.log                   # 分析日志
│   ├── 📄 modeling.log                   # 建模日志
│   └── 📄 application.log                # 应用日志
├── 📁 environment/                       # 环境配置
│   ├── 📄 requirements.txt               # Python依赖
│   ├── 📄 environment.yml                # Conda环境
│   ├── 📄 Dockerfile                     # Docker配置
│   └── 📄 .env.example                   # 环境变量示例
├── 📁 examples/                          # 使用示例
│   ├── 📄 basic_usage.py                 # 基础使用示例
│   ├── 📄 advanced_analysis.py           # 高级分析示例
│   └── 📄 custom_analysis.py             # 自定义分析示例
├── 📄 main.py                            # 项目主入口
├── 📄 run_analysis.py                    # 分析流程入口
├── 📄 setup.py                           # 项目安装配置
├── 📄 pyproject.toml                     # 项目构建配置
├── 📄 .gitignore                         # Git忽略配置
├── 📄 .pre-commit-config.yaml            # 代码检查配置
├── 📄 LICENSE                            # 许可证
└── 📄 README.md                          # 项目说明文档

# 函数

## 📁 src/data/ - 数据处理模块

### data_loader.py

python

```
load_csv_data()
load_excel_data()
load_database_data()
load_all_raw_data()
validate_data_schema()
check_file_exists()
get_data_statistics()
```



### data_cleaner.py

python

```
handle_missing_values()
remove_duplicates()
fix_data_types()
standardize_text_fields()
normalize_dates()
detect_outliers()
clean_user_data()
clean_order_data()
clean_product_data()
```



### data_validator.py

python

```
validate_data_quality()
check_data_integrity()
validate_user_ids()
validate_order_consistency()
generate_quality_report()
```



### data_transformer.py

python

```
merge_datasets()
pivot_data()
aggregate_data()
filter_data()
sort_data()
group_data()
```



### feature_engineer.py

python

```
create_user_features()
create_product_features()
create_temporal_features()
calculate_rfm_features()
create_interaction_features()
normalize_features()
select_features()
```



## 📁 src/analysis/ - 分析模块

### exploratory_analysis.py

python

```
explore_data_distribution()
analyze_correlations()
check_data_skewness()
identify_patterns()
summarize_numerical_data()
summarize_categorical_data()
generate_exploratory_report()
```



### user_analysis.py

python

```
calculate_user_metrics()
segment_users_rfm()
analyze_user_retention()
calculate_user_lifetime_value()
analyze_user_behavior()
identify_user_cohorts()
track_user_journey()
predict_user_churn()
```



### sales_analysis.py

python

```
analyze_sales_trends()
calculate_sales_metrics()
identify_seasonal_patterns()
forecast_sales()
analyze_sales_by_region()
compare_sales_performance()
detect_sales_anomalies()
```



### product_analysis.py

python

```
perform_abc_analysis()
analyze_product_performance()
calculate_product_metrics()
identify_product_associations()
analyze_price_elasticity()
track_inventory_turnover()
recommend_products()
```



### statistical_analysis.py

python

```
calculate_descriptive_stats()
perform_hypothesis_testing()
calculate_confidence_intervals()
analyze_variance()
perform_regression_analysis()
calculate_correlations()
```



### cohort_analysis.py

python

```
create_cohorts()
calculate_cohort_metrics()
analyze_cohort_retention()
track_cohort_performance()
visualize_cohort_analysis()
```



## 📁 src/modeling/ - 建模模块

### clustering.py

python

```
cluster_users()
cluster_products()
determine_optimal_clusters()
evaluate_clustering()
interpret_clusters()
```



### classification.py

python

```
train_churn_model()
predict_customer_segment()
classify_products()
evaluate_classification()
cross_validate_model()
```



### regression.py

python

```
train_sales_forecast()
predict_customer_value()
analyze_feature_importance()
evaluate_regression()
```



### time_series.py

python

```
decompose_time_series()
detect_trends()
identify_seasonality()
forecast_future_values()
validate_forecast()
```



### model_evaluation.py

python

```
calculate_model_metrics()
plot_confusion_matrix()
calculate_feature_importance()
perform_cross_validation()
compare_models()
```



## 📁 src/visualization/ - 可视化模块

### exploratory_charts.py

python

```
plot_distribution()
plot_correlation_heatmap()
create_scatter_plot()
plot_box_whisker()
create_histogram()
```



### business_charts.py

python

```
plot_sales_trend()
create_rfm_matrix()
plot_user_retention()
create_funnel_chart()
plot_geographic_distribution()
```



### dashboard_components.py

python

```
create_kpi_cards()
build_sales_dashboard()
build_user_dashboard()
build_product_dashboard()
create_interactive_filters()
```



### report_templates.py

python

```
generate_executive_summary()
create_detailed_report()
build_technical_report()
format_business_recommendations()
export_to_pdf()
```



### style_config.py

python

```
set_plot_style()
define_color_palette()
configure_fonts()
set_chart_sizes()
create_custom_themes()
```



## 📁 src/utils/ - 工具模块

### config_loader.py

python

```
load_analysis_config()
get_modeling_config()
read_visualization_config()
parse_data_config()
load_path_config()
```



### logger.py

python

```
setup_logging()
log_data_processing()
log_analysis_steps()
log_model_training()
log_errors()
```



### helpers.py

python

```
format_currency()
calculate_percentages()
date_range_generator()
data_sampler()
memory_optimizer()
```



### constants.py

python

```
define_data_columns()
set_analysis_parameters()
configure_model_settings()
define_color_codes()
```



### decorators.py

python

```
timer_decorator()
cache_decorator()
validation_decorator()
log_decorator()
retry_decorator()
```



## 📁 src/scripts/ - 执行脚本模块

### run_data_pipeline.py

python

```
execute_data_loading()
run_data_cleaning()
perform_feature_engineering()
validate_data_pipeline()
```



### run_user_analysis.py

python

```
analyze_user_demographics()
calculate_user_metrics()
segment_user_base()
generate_user_insights()
```



### run_sales_analysis.py

python

```
analyze_sales_performance()
track_sales_trends()
forecast_future_sales()
generate_sales_reports()
```



### run_product_analysis.py

python

```
categorize_products()
analyze_product_sales()
identify_top_products()
generate_product_recommendations()
```



### run_full_analysis.py

python

```
execute_complete_analysis()
coordinate_all_modules()
generate_comprehensive_report()
```



### generate_reports.py

python

```
compile_all_insights()
create_executive_dashboard()
generate_business_recommendations()
export_final_reports()
```



## 📄 根目录主文件函数

### main.py

python

```
initialize_analysis()
setup_environment()
execute_main_pipeline()
handle_exceptions()
shutdown_cleanly()
```



### run_analysis.py

python

```
run_quick_analysis()
run_comprehensive_analysis()
run_custom_analysis()
```



## 📁 config/ - 配置相关函数

### 配置加载函数

python

```
get_analysis_parameters()
load_model_configurations()
get_visualization_settings()
read_data_paths()
validate_configurations()
```



## 📁 tests/ - 测试函数

### 测试函数

python

```
test_data_loading()
test_data_cleaning()
test_analysis_functions()
test_model_performance()
test_visualization_output()
test_integration()
```



# 类结构

## 📁 src/data/ - 数据处理模块

### data_loader.py
```python
class DataLoader:
    def __init__(self, base_path: str = "./data/raw"):
        self.base_path = base_path
        self.loaded_data = {}
    
    def load_csv_data(self, filename: str) -> pd.DataFrame:
        """加载CSV文件"""
    
    def load_excel_data(self, filename: str) -> pd.DataFrame:
        """加载Excel文件"""
    
    def load_all_raw_data(self) -> dict:
        """加载所有原始数据"""
    
    def validate_data_schema(self, df: pd.DataFrame, expected_schema: dict) -> bool:
        """验证数据模式"""
    
    def get_data_statistics(self) -> dict:
        """获取数据统计信息"""
```

### data_cleaner.py
```python
class DataCleaner:
    def __init__(self, cleaning_config: dict = None):
        self.config = cleaning_config or {}
        self.cleaning_report = {}
    
    def clean_user_data(self, users_df: pd.DataFrame) -> pd.DataFrame:
        """清洗用户数据"""
    
    def clean_order_data(self, orders_df: pd.DataFrame) -> pd.DataFrame:
        """清洗订单数据"""
    
    def clean_product_data(self, products_df: pd.DataFrame) -> pd.DataFrame:
        """清洗产品数据"""
    
    def handle_missing_values(self, df: pd.DataFrame, strategy: str = 'auto') -> pd.DataFrame:
        """处理缺失值"""
    
    def remove_duplicates(self, df: pd.DataFrame, subset: list = None) -> pd.DataFrame:
        """删除重复记录"""
    
    def generate_quality_report(self) -> dict:
        """生成质量报告"""
```

### data_validator.py
```python
class DataValidator:
    def __init__(self, validation_rules: dict = None):
        self.rules = validation_rules or {}
        self.validation_results = {}
    
    def validate_data_quality(self, df: pd.DataFrame, data_type: str) -> dict:
        """验证数据质量"""
    
    def check_data_integrity(self, datasets: dict) -> dict:
        """检查数据完整性"""
    
    def validate_user_ids(self, users_df: pd.DataFrame, orders_df: pd.DataFrame) -> bool:
        """验证用户ID一致性"""
    
    def generate_validation_report(self) -> dict:
        """生成验证报告"""
```

### data_transformer.py
```python
class DataTransformer:
    def __init__(self):
        self.transformation_log = []
    
    def merge_datasets(self, left_df: pd.DataFrame, right_df: pd.DataFrame, on: str) -> pd.DataFrame:
        """合并数据集"""
    
    def pivot_data(self, df: pd.DataFrame, index: list, columns: str, values: str) -> pd.DataFrame:
        """数据透视"""
    
    def aggregate_data(self, df: pd.DataFrame, group_by: list, aggregations: dict) -> pd.DataFrame:
        """数据聚合"""
    
    def filter_data(self, df: pd.DataFrame, conditions: dict) -> pd.DataFrame:
        """数据筛选"""
```

### feature_engineer.py
```python
class FeatureEngineer:
    def __init__(self):
        self.features_created = []
        self.feature_descriptions = {}
    
    def create_user_features(self, users_df: pd.DataFrame, orders_df: pd.DataFrame) -> pd.DataFrame:
        """创建用户特征"""
    
    def create_product_features(self, products_df: pd.DataFrame, orders_df: pd.DataFrame) -> pd.DataFrame:
        """创建产品特征"""
    
    def create_temporal_features(self, df: pd.DataFrame, date_column: str) -> pd.DataFrame:
        """创建时间特征"""
    
    def create_rfm_features(self, orders_df: pd.DataFrame, current_date: str = None) -> pd.DataFrame:
        """创建RFM特征"""
    
    def calculate_feature_correlations(self, features_df: pd.DataFrame) -> pd.DataFrame:
        """计算特征相关性"""
```

## 📁 src/analysis/ - 分析模块

### exploratory_analysis.py
```python
class ExploratoryAnalyzer:
    def __init__(self):
        self.analysis_results = {}
        self.insights = []
    
    def analyze_data_distribution(self, df: pd.DataFrame) -> dict:
        """分析数据分布"""
    
    def calculate_correlations(self, df: pd.DataFrame) -> pd.DataFrame:
        """计算相关性矩阵"""
    
    def identify_outliers(self, df: pd.DataFrame, columns: list) -> dict:
        """识别异常值"""
    
    def generate_summary_statistics(self, df: pd.DataFrame) -> dict:
        """生成汇总统计"""
    
    def create_exploratory_report(self) -> dict:
        """创建探索性分析报告"""
```

### user_analysis.py
```python
class UserAnalyzer:
    def __init__(self, config: dict = None):
        self.config = config or {}
        self.analysis_results = {}
    
    def calculate_rfm_metrics(self, orders_df: pd.DataFrame, current_date: str = None) -> pd.DataFrame:
        """计算RFM指标"""
    
    def segment_users(self, rfm_df: pd.DataFrame) -> pd.DataFrame:
        """用户分群"""
    
    def analyze_user_retention(self, users_df: pd.DataFrame, orders_df: pd.DataFrame) -> pd.DataFrame:
        """分析用户留存"""
    
    def calculate_user_lifetime_value(self, users_df: pd.DataFrame, orders_df: pd.DataFrame) -> pd.DataFrame:
        """计算用户生命周期价值"""
    
    def analyze_user_behavior(self, behavior_df: pd.DataFrame) -> dict:
        """分析用户行为"""
    
    def get_user_insights(self) -> dict:
        """获取用户洞察"""
```

### sales_analysis.py
```python
class SalesAnalyzer:
    def __init__(self):
        self.sales_trends = {}
        self.performance_metrics = {}
    
    def analyze_sales_trends(self, orders_df: pd.DataFrame, frequency: str = 'M') -> pd.DataFrame:
        """分析销售趋势"""
    
    def calculate_sales_metrics(self, orders_df: pd.DataFrame) -> dict:
        """计算销售指标"""
    
    def identify_seasonal_patterns(self, sales_data: pd.DataFrame) -> dict:
        """识别季节性模式"""
    
    def analyze_sales_by_region(self, orders_df: pd.DataFrame, users_df: pd.DataFrame) -> dict:
        """按地区分析销售"""
    
    def compare_performance(self, sales_data: pd.DataFrame, dimension: str) -> pd.DataFrame:
        """性能比较"""
```

### product_analysis.py
```python
class ProductAnalyzer:
    def __init__(self):
        self.product_categories = {}
        self.performance_analysis = {}
    
    def perform_abc_analysis(self, products_df: pd.DataFrame, sales_df: pd.DataFrame) -> pd.DataFrame:
        """执行ABC分析"""
    
    def analyze_product_performance(self, products_df: pd.DataFrame, orders_df: pd.DataFrame) -> dict:
        """分析产品表现"""
    
    def calculate_product_metrics(self, products_df: pd.DataFrame, sales_df: pd.DataFrame) -> pd.DataFrame:
        """计算产品指标"""
    
    def identify_product_associations(self, orders_df: pd.DataFrame) -> dict:
        """识别产品关联"""
    
    def analyze_price_elasticity(self, products_df: pd.DataFrame, sales_df: pd.DataFrame) -> dict:
        """分析价格弹性"""
```

### statistical_analysis.py
```python
class StatisticalAnalyzer:
    def __init__(self):
        self.test_results = {}
    
    def calculate_descriptive_stats(self, df: pd.DataFrame) -> dict:
        """计算描述性统计"""
    
    def perform_hypothesis_testing(self, data1: pd.Series, data2: pd.Series, test_type: str) -> dict:
        """执行假设检验"""
    
    def calculate_confidence_intervals(self, data: pd.Series, confidence: float = 0.95) -> dict:
        """计算置信区间"""
    
    def analyze_variance(self, data: pd.DataFrame, group_column: str, value_column: str) -> dict:
        """方差分析"""
```

### cohort_analysis.py
```python
class CohortAnalyzer:
    def __init__(self):
        self.cohort_data = {}
    
    def create_cohorts(self, users_df: pd.DataFrame, orders_df: pd.DataFrame, period: str = 'M') -> pd.DataFrame:
        """创建同期群"""
    
    def calculate_cohort_retention(self, cohort_df: pd.DataFrame) -> pd.DataFrame:
        """计算群组留存率"""
    
    def analyze_cohort_behavior(self, cohort_df: pd.DataFrame) -> dict:
        """分析群组行为"""
    
    def track_cohort_performance(self, cohort_df: pd.DataFrame, metric: str) -> pd.DataFrame:
        """跟踪群组表现"""
```

## 📁 src/modeling/ - 建模模块

### clustering.py
```python
class UserClustering:
    def __init__(self, n_clusters: int = 4):
        self.n_clusters = n_clusters
        self.model = None
        self.cluster_labels = None
    
    def prepare_features(self, user_data: pd.DataFrame) -> pd.DataFrame:
        """准备聚类特征"""
    
    def fit_clusters(self, features: pd.DataFrame):
        """拟合聚类模型"""
    
    def predict_clusters(self, features: pd.DataFrame) -> np.array:
        """预测聚类"""
    
    def analyze_clusters(self, user_data: pd.DataFrame, cluster_labels: np.array) -> dict:
        """分析聚类结果"""
    
    def get_cluster_profiles(self) -> dict:
        """获取群组画像"""
```

### classification.py
```python
class ChurnPredictor:
    def __init__(self, model_type: str = 'random_forest'):
        self.model_type = model_type
        self.model = None
        self.feature_importance = {}
    
    def prepare_training_data(self, users_df: pd.DataFrame, orders_df: pd.DataFrame) -> tuple:
        """准备训练数据"""
    
    def train_model(self, X_train: pd.DataFrame, y_train: pd.Series):
        """训练模型"""
    
    def predict_churn_probability(self, user_features: pd.DataFrame) -> np.array:
        """预测流失概率"""
    
    def evaluate_model(self, X_test: pd.DataFrame, y_test: pd.Series) -> dict:
        """评估模型性能"""
```

### regression.py
```python
class SalesPredictor:
    def __init__(self, model_type: str = 'linear'):
        self.model_type = model_type
        self.model = None
        self.prediction_results = {}
    
    def prepare_regression_data(self, sales_data: pd.DataFrame, features: list) -> tuple:
        """准备回归数据"""
    
    def train_regression_model(self, X_train: pd.DataFrame, y_train: pd.Series):
        """训练回归模型"""
    
    def predict_sales(self, features: pd.DataFrame) -> np.array:
        """预测销售"""
    
    def analyze_feature_importance(self) -> dict:
        """分析特征重要性"""
```

### time_series.py
```python
class TimeSeriesAnalyzer:
    def __init__(self, model_type: str = 'arima'):
        self.model_type = model_type
        self.model = None
        self.forecast_results = {}
    
    def prepare_time_series(self, sales_data: pd.DataFrame, date_column: str, value_column: str) -> pd.Series:
        """准备时间序列数据"""
    
    def decompose_time_series(self, time_series: pd.Series) -> dict:
        """时间序列分解"""
    
    def train_forecast_model(self, time_series: pd.Series):
        """训练预测模型"""
    
    def forecast_future_values(self, periods: int = 12) -> pd.DataFrame:
        """预测未来值"""
```

### model_evaluation.py
```python
class ModelEvaluator:
    def __init__(self):
        self.evaluation_metrics = {}
    
    def calculate_classification_metrics(self, y_true: np.array, y_pred: np.array) -> dict:
        """计算分类指标"""
    
    def calculate_regression_metrics(self, y_true: np.array, y_pred: np.array) -> dict:
        """计算回归指标"""
    
    def perform_cross_validation(self, model, X: pd.DataFrame, y: pd.Series, cv: int = 5) -> dict:
        """执行交叉验证"""
    
    def plot_confusion_matrix(self, y_true: np.array, y_pred: np.array) -> plt.Figure:
        """绘制混淆矩阵"""
    
    def generate_evaluation_report(self) -> dict:
        """生成评估报告"""
```

## 📁 src/visualization/ - 可视化模块

### exploratory_charts.py
```python
class ExploratoryCharts:
    def __init__(self, style: str = 'seaborn'):
        self.style = style
        self.set_style()
    
    def set_style(self):
        """设置图表样式"""
    
    def plot_distribution(self, data: pd.Series, title: str) -> plt.Figure:
        """绘制分布图"""
    
    def plot_correlation_heatmap(self, data: pd.DataFrame, title: str) -> plt.Figure:
        """绘制相关性热力图"""
    
    def create_scatter_plot(self, data: pd.DataFrame, x: str, y: str, title: str) -> plt.Figure:
        """创建散点图"""
    
    def plot_box_whisker(self, data: pd.DataFrame, columns: list, title: str) -> plt.Figure:
        """绘制箱线图"""
```

### business_charts.py
```python
class BusinessCharts:
    def __init__(self):
        self.chart_templates = {}
    
    def create_sales_trend_chart(self, sales_data: pd.DataFrame) -> plt.Figure:
        """创建销售趋势图"""
    
    def create_rfm_matrix(self, rfm_data: pd.DataFrame) -> plt.Figure:
        """创建RFM矩阵图"""
    
    def plot_user_retention(self, retention_data: pd.DataFrame) -> plt.Figure:
        """绘制用户留存图"""
    
    def create_funnel_chart(self, funnel_data: pd.DataFrame) -> plt.Figure:
        """创建漏斗图"""
    
    def plot_geographic_distribution(self, geo_data: pd.DataFrame) -> plt.Figure:
        """绘制地理分布图"""
```

### dashboard_components.py
```python
class DashboardCreator:
    def __init__(self, title: str = "电商数据分析仪表板"):
        self.title = title
        self.components = []
    
    def add_kpi_card(self, title: str, value: any, change: float = None):
        """添加KPI卡片"""
    
    def add_chart_component(self, chart: plt.Figure, title: str, position: tuple):
        """添加图表组件"""
    
    def create_sales_dashboard(self, sales_data: pd.DataFrame, metrics: dict) -> dict:
        """创建销售仪表板"""
    
    def create_user_dashboard(self, user_analysis: dict) -> dict:
        """创建用户仪表板"""
    
    def export_dashboard(self, format: str = 'html'):
        """导出仪表板"""
```

### report_templates.py
```python
class ReportGenerator:
    def __init__(self, template: str = 'default'):
        self.template = template
        self.sections = []
    
    def add_executive_summary(self, key_metrics: dict, insights: list):
        """添加执行摘要"""
    
    def add_analysis_section(self, title: str, content: any, charts: list = None):
        """添加分析章节"""
    
    def add_recommendations(self, recommendations: list):
        """添加建议"""
    
    def generate_pdf_report(self, output_path: str):
        """生成PDF报告"""
    
    def generate_html_report(self, output_path: str):
        """生成HTML报告"""
```

### style_config.py
```python
class StyleConfig:
    def __init__(self):
        self.color_palettes = {}
        self.font_settings = {}
        self.chart_sizes = {}
    
    def set_color_palette(self, palette_name: str, colors: list):
        """设置颜色调色板"""
    
    def configure_fonts(self, font_family: str, font_sizes: dict):
        """配置字体"""
    
    def set_chart_sizes(self, sizes: dict):
        """设置图表尺寸"""
    
    def create_custom_theme(self, theme_name: str, settings: dict):
        """创建自定义主题"""
```

## 📁 src/utils/ - 工具模块

### config_loader.py
```python
class ConfigManager:
    def __init__(self, config_path: str = "./config"):
        self.config_path = config_path
        self.configs = {}
    
    def load_analysis_config(self) -> dict:
        """加载分析配置"""
    
    def load_modeling_config(self) -> dict:
        """加载建模配置"""
    
    def load_visualization_config(self) -> dict:
        """加载可视化配置"""
    
    def get_config(self, config_type: str) -> dict:
        """获取配置"""
    
    def update_config(self, config_type: str, updates: dict):
        """更新配置"""
```

### logger.py
```python
class AnalysisLogger:
    def __init__(self, log_level: str = 'INFO', log_file: str = None):
        self.log_level = log_level
        self.log_file = log_file
        self.setup_logger()
    
    def setup_logger(self):
        """设置日志记录器"""
    
    def log_info(self, message: str):
        """记录信息日志"""
    
    def log_warning(self, message: str):
        """记录警告日志"""
    
    def log_error(self, message: str, exception: Exception = None):
        """记录错误日志"""
    
    def log_analysis_step(self, step_name: str, status: str):
        """记录分析步骤"""
```

### helpers.py
```python
class HelperFunctions:
    @staticmethod
    def format_currency(amount: float) -> str:
        """格式化货币"""
    
    @staticmethod
    def calculate_percentage_change(old_value: float, new_value: float) -> float:
        """计算百分比变化"""
    
    @staticmethod
    def date_range_generator(start_date: str, end_date: str, frequency: str) -> list:
        """生成日期范围"""
    
    @staticmethod
    def optimize_dataframe_memory(df: pd.DataFrame) -> pd.DataFrame:
        """优化DataFrame内存使用"""
```

### constants.py
```python
class AnalysisConstants:
    """分析常量定义"""
    
    # 用户分群阈值
    RFM_THRESHOLDS = {
        'high_value': 12,
        'potential': 9,
        'general': 6
    }
    
    # ABC分析参数
    ABC_PERCENTAGES = {
        'A_class': 0.8,
        'B_class': 0.95
    }
    
    # 时间频率
    TIME_FREQUENCIES = ['D', 'W', 'M', 'Q', 'Y']
```

### decorators.py
```python
class AnalysisDecorators:
    @staticmethod
    def timer_decorator(func):
        """计时装饰器"""
    
    @staticmethod
    def cache_decorator(func):
        """缓存装饰器"""
    
    @staticmethod
    def validation_decorator(func):
        """验证装饰器"""
    
    @staticmethod
    def log_decorator(func):
        """日志装饰器"""
```

## 📁 src/scripts/ - 执行脚本

### run_data_pipeline.py
```python
class DataPipeline:
    def __init__(self):
        self.data_loader = DataLoader()
        self.data_cleaner = DataCleaner()
        self.feature_engineer = FeatureEngineer()
    
    def execute_data_loading(self) -> dict:
        """执行数据加载"""
    
    def run_data_cleaning(self) -> dict:
        """运行数据清洗"""
    
    def perform_feature_engineering(self) -> dict:
        """执行特征工程"""
    
    def run_full_pipeline(self) -> dict:
        """运行完整管道"""
```

### run_user_analysis.py
```python
class UserAnalysisPipeline:
    def __init__(self):
        self.user_analyzer = UserAnalyzer()
        self.cohort_analyzer = CohortAnalyzer()
    
    def analyze_user_demographics(self) -> dict:
        """分析用户人口统计"""
    
    def perform_user_segmentation(self) -> dict:
        """执行用户分群"""
    
    def calculate_user_metrics(self) -> dict:
        """计算用户指标"""
    
    def generate_user_insights(self) -> dict:
        """生成用户洞察"""
```

## 📄 根目录主文件

### main.py
```python
class ECommerceAnalysisOrchestrator:
    """电商分析协调器 - 主类"""
    
    def __init__(self, project_root: str = "."):
        self.project_root = project_root
        self.config_manager = ConfigManager(f"{project_root}/config")
        self.data_pipeline = DataPipeline()
        self.user_analyzer = UserAnalyzer()
        self.sales_analyzer = SalesAnalyzer()
        self.logger = AnalysisLogger()
    
    def initialize_analysis(self):
        """初始化分析环境"""
    
    def run_data_preparation(self) -> dict:
        """运行数据准备"""
    
    def run_user_analysis(self) -> dict:
        """运行用户分析"""
    
    def run_sales_analysis(self) -> dict:
        """运行销售分析"""
    
    def run_product_analysis(self) -> dict:
        """运行产品分析"""
    
    def generate_comprehensive_report(self) -> dict:
        """生成综合报告"""
    
    def run_full_analysis(self) -> dict:
        """运行完整分析"""
```
