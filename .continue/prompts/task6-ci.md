---
name: task6-ci
description: 教程模式：配置 GitHub Actions CI
invokable: true
---

请用教程模式讲解“任务 6：配置 GitHub Actions CI”。

必须按以下顺序回答：

# 先做什么
先告诉学生：
- 这一步是把前面的验证自动化
- 本地能跑不代表真正交付完成

# 需要修改的文件
必须覆盖：
- .github/workflows/ci.yml

# 可直接使用的代码
给出尽量完整、可直接使用的 workflow 代码，至少包含：
- backend-unit-tests
- backend-api-tests
- frontend-tests

# 做完后怎么验证
优先给出：
- make check-task-6
- git push
- 打开 GitHub Actions 页面确认运行结果

# 再讲清楚为什么这样写
必须解释：
- jobs 和 steps 分别负责什么
- 为什么 push / pull_request 都要触发
- 为什么 CI 是工程流程的一部分
