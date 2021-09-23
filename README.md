# DementiaChatBot
## 项目介绍
该ChatBot旨在解决际代沟通问题，为痴呆患者提供更多的社会互动机会，在交流过程中增强积极情感。ChatBot根据家属提供的患者个人信息生成个性化多轮问答与患者进行聊天；并对聊天数据进行分析，评估患者在聊到特定话题时的情绪状态和感兴趣程度，向家属推荐话题。
## 项目架构
项目采用C/S模式，客户端适用Android系统，使用科大讯飞的听写API实现语音识别与生成，采用OkHttp进行网络请求；服务器端使用Flask处理客户端请求，连接MongoDB进行数据的增删改查。

Android客户端地址：https://github.com/Zx1999/DementiaChatBotApp
