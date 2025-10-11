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