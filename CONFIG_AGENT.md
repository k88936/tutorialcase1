# 配置ai助教说明
我们使用的工具是 `continue` [(文档)](https://docs.continue.dev/ide-extensions/install)

这个产品工具免费，额度收费，但支持BYOK（bring your own key）我们不必注册，使用我们自己的apkey。

## bring your own key
我们知道可以用`model name`，`base url`，和`api key`来使用与openai兼容的第三方服务商，这里我们介绍一些，方便同学使用。

* 学校的算力券  
    > 提示 这个平台提供的文档语焉不详，还有错误，请仔细阅读。  

    1. 通过学校的入口[登录](https://easycompute.cs.tsinghua.edu.cn/home)   
    2. 在[模型页面](https://ai.paratera.com/#/lms/model)可以挑选模型，查看简介。
    3. `model name` 是红色圈里的字符串
    4. `base url` 经过验证使用`https://llmapi.paratera.com`
    5. `api key`[申请](https://ai.paratera.com/#/lms/api)

* 阿里云
    > 提示 阿里云需要实名认证，嫌麻烦的同学使用学校的算力券就好.  
    > 阿里云对于大部分模型提供了90天一定量的免费额度，足够我们课程使用.

    1. [模型选择页](https://bailian.console.aliyun.com/cn-beijing?tab=model#/model-market/all) 
    2. 详情页面
    3. `model name` 可以直接复制这里
    4. `base url` `https://dashscope.aliyuncs.com/compatible-mode/v1`
    5. `api key` [申请](https://bailian.console.aliyun.com/?tab=model#/api-key)


> 可以对比下两者，良好的文档是很重要的

## config continu

1. 在vscode的插件管理中搜索并安装continue
把`.continue/agents/config-example.yaml`复制一份到`.continue/agents/config.yaml`. 
2. 然后修改: 替换 `MODEL_NAME` `API_BASE_URL` `API_KEY`

> 我们做一次复制的目的是已经把`.continue/agents/config.yaml`加入gitignore中，避免同学不小心提交了配置文件导致apikey泄露。  
> 更安全的方法是使用环境变量，这里我们从简。

3. 然后我们在continue的配置选择里选择我们的config.yaml 

## hello software engineering