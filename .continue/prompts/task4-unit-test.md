---
name: task4-unit-test
description: 教程模式：编写后端单元测试
invokable: true
---

请用教程模式讲解“任务 4：编写后端单元测试”。

必须按以下顺序回答：

# 先做什么
先告诉学生：
- 这一步是在验证 controller 层逻辑
- 要先准备测试数据，再调用 get_post_detail()

# 需要修改的文件
必须覆盖：
- backend/tests/test_post_detail.py

# 可直接使用的代码
给出尽量完整、可直接使用的测试代码，至少覆盖：
- success
- not_found
- reply 顺序 / root replyId 为 0

# 做完后怎么验证
优先给出：
- make check-task-4
- cd backend && python manage.py test --filter tests.test_post_detail

# 再讲清楚为什么这样写
必须解释：
- controller test 在测什么
- 为什么它和 API test 不一样
- 为什么至少要覆盖 success / not_found / replyId 三条路径
