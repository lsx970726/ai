# ai 目录结构

本项目使用Langchain框架构建了一个全栈AI问答系统，够能实时回答此刻各大主流媒体、热搜等趋势。
目录结构如下:  
ai/  
├── UI/ # React前端页面  
│ ├── public/ # 静态文件  
│ ├── src/ # React源码  
│ └── package.json # 项目依赖配置  
├── backend/ # 后端GraphQL、API  
│ ├── app.py # 主应用入口  
│ └── utils/ # 工具模块  
│ └── schemas/ #  GraphQL 的模式定义  
├── ChatGLM3/ # ChatGLM3问答  
│ ├── agents/ # 自定义Agent  
│ ├── models/ # 模型加载、微调代码  
│ └── data/ # 数据存储、预处理代码  
├── collection/ # 实时内容采集  
│ └── data/ # PostgreSQL数据存储、预处理代码  
├── kafka/ # 消息队列  
│ └── data/ # Kafka数据存储、预处理代码  
├── log/ # 日志文件  
├── tests/ # 测试用例  
├── config/ # 配置文件  
├── docs/ # 文档  
├── scripts/ # 脚本  
│ └── db_move.sh # 数据库迁移  
│ └── clean.sh # 清理  
│ └── backup.sh # 备份  
├── Dockerfile  # docker支持  
│ └── docker-compose.yml    # docker-compose支持  
├── .env # 环境变量  
├── .gitignore # 忽略文件  
├── start.sh # 运行  
├── stop.sh # 停止  
└── requirements.txt  # 依赖 





# 后续可考虑的升级点  
1. 多种技术的混合方案,例如基于Flask提供标准RESTful API,同时支持GraphQL查询、利用Kafka实现异步任务和事件驱动等。
2. Prometheus + Grafana 监控和日志记录
3. 引入Elasticsearch + Kibana + Logstash + Filebeat
4. 引入Redis + Celery
5. 引入MongoDB
6. 引入Minio
7. 为实现自动化构建、测试和部署,可以引入CI/CD工具,如Jenkins、GitHub Actions等。