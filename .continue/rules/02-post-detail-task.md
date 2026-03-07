---
name: Post Detail Assignment Rules
---

当前作业是：恢复并完善“帖子详情”功能。

任务目标：

1. 理解帖子详情接口路径
2. 实现 backend/post/controllers.py 中的 get_post_detail(post_id)
3. 实现 backend/post/views.py 中的 PostDetailView.get()
4. 实现 frontend/src/post/post_detail_page.tsx 中的 loadPost()
5. 通过后端 unittest
6. 通过前端测试
7. 通过 GitHub Actions

本项目中，帖子详情接口对应路径是：
api/v1/post/<int:postId>

学生应满足的行为约束：

- 帖子存在时：
  - 后端返回 200
  - 返回详情对象
  - reply 字段为数组
- 帖子不存在时：
  - 后端返回 404
  - 返回 {"message": "not found"}
- 前端页面：
  - 成功时显示帖子标题
  - 失败时显示错误信息
  - 加载中显示骨架
- 不要改动接口路径
- 不要改动已有的整体页面结构，优先补全缺失逻辑

这和现有后端代码对齐：详情接口路由在 api/v1/post/<int:postId>，PostDetailView 文档也声明了 404 响应。
