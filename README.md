# 时事新闻问答系统

## 项目介绍

基于Langchain框架的全栈项目，实现一个基于时事的新闻问答系统。

## 项目路径规划

### 第一阶段: 原型开发(Demo)（2024.03.28-）

#### ChatGLM3 问答模块

在 chatglm3/agents/ 中创建自定义 LangChain Agent,调用chatglm3的api，集成问答功能
使用 Streamlit/Gradio 快速构建交互式 Demo 界面
#### 基础后端 API
在 backend/ 下使用 Flask/FastAPI 搭建基础的 RESTful API
实现简单的身份验证 (Session/JWT)
API 路由: /query (问答查询接口)
#### React 前端原型

在 UI/ 下用 Create React App 建立基础的 React 应用
实现基本的路由和页面布局
使用 Axios 调用后端 API 获取问答结果,并渲染到界面
### 第二阶段: 前后端对接

#### 数据库集成

在 collection/data/ 下设置 PostgreSQL 数据库
使用 SQLAlchemy/Django ORM 与数据库交互
存储用户查询记录、聊天记录等结构化数据
#### GraphQL API

在 backend/schemas/ 中定义 GraphQL 模式
使用 Ariadne/Graphene 等库实现 GraphQL 查询解析
前端使用 Apollo Client 或 Relay 调用 GraphQL API
#### 消息队列&异步任务

使用 Kafka 构建消息队列系统,存储在 kafka/data/
使用 Celery/RQ 实现异步任务处理
后端将问答查询任务加入队列,由异步 Worker 处理
#### 前端状态管理&优化

使用 Redux/MobX 管理前端应用状态
实现查询状态显示(加载中、出错等)
性能优化(代码分割、懒加载等)
### 第三阶段: 系统完善和测试

#### 数据收集与预处理

使用 Scrapy/BeautifulSoup 抓取实时新闻等数据源
使用 NLTK/SpaCy 进行文本预处理和特征提取
数据存储在 collection/data/ 下的 PostgreSQL
#### 语义搜索引擎

使用 Haystack/FAISS 构建语义搜索引擎
整合从多源收集的文本数据,建立语义索引
在 chatglm3/agents/ 中将搜索结果作为一个工具传递给 Agent
#### 系统测试

使用 Pytest/Unittest 编写单元测试,测试 API、模型等
使用 Selenium 进行功能测试和 UI 自动化测试
部署到测试环境,进行综合系统测试
#### 监控和日志分析

使用 Prometheus 和 Grafana 监控系统运行状况
使用 ELK Stack 收集和分析应用日志,存储在 log/ 下
#### CI/CD 与部署

使用 GitLab CI/CD 或 GitHub Actions 实现持续集成和交付
编写 Dockerfile 和 docker-compose.yml 实现容器化部署
部署到 Kubernetes 集群或云服务提供商进行负载测试
#### 文档与协作

使用 Notion/GitBook 等文档工具编写开发文档,存储在 docs/
使用 Trello/Github Projects/Asana 等项目管理工具,规划和跟踪自己的开发进度
可选择使用 Obsidian 等知识管理工具,梳理和总结所学知识