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