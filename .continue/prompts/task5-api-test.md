---
name: task5-api-test
description: 教程模式：编写 API 测试
invokable: true
---

请用教程模式讲解“任务 5：编写 API 测试”。

必须按以下顺序回答：

# 先做什么
先告诉学生：
- 这一步是在验证真实 HTTP 接口，而不是只调 controller
- 要用测试 client 访问后端路由

# 需要修改的文件
必须覆盖：
- backend/tests/test_post_detail_api.py

# 可直接使用的代码
给出尽量完整、可直接使用的 API 测试代码，至少覆盖：
- 200
- 404
- 未登录

# 做完后怎么验证
优先给出：
- make check-task-5
- cd backend && python manage.py test --filter tests.test_post_detail_api

# 再讲清楚为什么这样写
必须解释：
- 为什么 API 测试要走 HTTP
- 为什么它和 controller test 不能互相替代
- 为什么要测状态码和 JSON 两类结果
