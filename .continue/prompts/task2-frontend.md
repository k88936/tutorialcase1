---
name: task2-frontend
description: 教程模式：完成前端帖子详情页加载
invokable: true
---

请用教程模式讲解“任务 2：完成前端帖子详情页加载”。

必须按以下顺序回答：

# 先做什么
先告诉学生：
- 这一步在前后端链路中的位置
- 现在要补的是页面里的 loadPost()

# 需要修改的文件
必须覆盖：
- frontend/src/post/post_detail_page.tsx
- frontend/src/backend.tsx

并说明：
- 页面文件负责状态和渲染
- backend.tsx 负责 API 封装

# 可直接使用的代码
给出尽量完整、可直接使用的代码，至少包括：
- loadPost()

# 做完后怎么验证
优先给出：
- make check-task-2
- cd frontend && CI=true npm test -- --watchAll=false --runInBand --testPathPattern=post_detail_page.test.tsx

# 再讲清楚为什么这样写
必须解释：
- 路由参数 postId 从哪里来
- 为什么要区分 loading / success / error
- 为什么未授权时要跳回首页
