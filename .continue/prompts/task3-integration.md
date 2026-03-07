---
name: task3-integration
description: 教程模式：完成前后端联调
invokable: true
---

请用教程模式讲解“任务 3：完成前后端联调”。

必须先给学生一份清晰的操作步骤，再讲原理。

必须覆盖以下内容：

# 先做什么
告诉学生：
1. 先启动 backend
2. 再启动 frontend
3. 打开 /post/1
4. 再打开一个不存在的帖子 ID
5. 打开浏览器 Network 面板

# 需要关注的文件
必须覆盖：
- frontend/package.json
- frontend/src/backend.tsx
- backend/post/urls.py

# 如何验证
优先给出：
- make check-task-3
- 手动打开 /post/1
- 手动访问一个不存在的帖子 ID
- Network 面板查看请求是否真的发到了后端

# 再讲清楚为什么这样工作
必须解释：
- CRA proxy 是什么
- 前端请求路径为什么能打到 Django
- 为什么联调不能只靠单元测试代替
