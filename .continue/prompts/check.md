---
name: check
description: 检查帖子详情任务完成度
invokable: true
---

请检查当前“帖子详情”作业的完成度。

优先使用以下思路：
1. 查看 backend/post/controllers.py 中 get_post_detail 是否已实现
2. 查看 backend/post/views.py 中 PostDetailView.get 是否已实现
3. 查看 frontend/src/post/post_detail_page.tsx 中 loadPost 是否已实现
4. 提醒学生运行：
   - cd backend && python manage.py test --filter tests.test_post_detail
   - cd frontend && CI=true npm test -- --watchAll=false --runInBand
5. 如果无法自动运行命令，就明确告诉学生下一条应该执行什么命令
6. 输出格式：
   - 已完成
   - 未完成
   - 下一步
