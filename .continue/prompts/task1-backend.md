---
name: task1-backend
description: 教程模式：实现后端帖子详情接口
invokable: true
---

请用教程模式讲解“任务 1：实现后端帖子详情接口”。

必须按以下顺序回答：

# 先做什么
先告诉学生：
- 这一步在整体链路里的位置
- 为什么要先看后端路由，再看 controller，再看 view

# 需要修改的文件
必须覆盖：
- backend/post/urls.py
- backend/post/controllers.py
- backend/post/views.py

并说明：
- urls.py 负责接口入口
- controllers.py 负责查询和组织数据
- views.py 负责 HTTP 状态码和响应

# 可直接使用的代码
给出尽量完整、可直接使用的代码，至少包括：
- get_post_detail(post_id)
- PostDetailView.get()

# 做完后怎么验证
优先给出：
- make check-task-1
- cd backend && python manage.py test --filter tests.test_post_detail

# 再讲清楚为什么这样写
必须解释：
- 为什么 controller 不直接负责 HTTP
- 为什么 view 不负责复杂查询
- 为什么帖子不存在应该返回 404，而不是 500
