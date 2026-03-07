# 作业：恢复帖子详情功能（教程模式）

## 目标
你需要恢复并完善论坛系统中的“帖子详情”功能，并完成从功能实现到测试与 CI 的完整工程流程。

## 课程任务
1. 实现后端帖子详情接口
2. 完成前端帖子详情页加载
3. 完成前后端联调
4. 编写后端单元测试
5. 编写 API 测试
6. 配置 GitHub Actions CI

## 重点文件
- backend/post/urls.py
- backend/post/views.py
- backend/post/controllers.py
- frontend/src/post/post_detail_page.tsx
- frontend/src/backend.tsx
- backend/tests/test_post_detail.py
- backend/tests/test_post_detail_api.py
- frontend/src/post/post_detail_page.test.tsx
- .github/workflows/ci.yml

## 推荐顺序
1. 任务 1
2. 任务 2
3. 任务 3
4. 任务 4
5. 任务 5
6. 任务 6

## 本地检查命令
- `make check-task-1`
- `make check-task-2`
- `make check-task-3`
- `make check-task-4`
- `make check-task-5`
- `make check-task-6`
- `make check-all`

## 常用测试命令
- `cd backend && python manage.py test --filter tests.test_post_detail`
- `cd backend && python manage.py test --filter tests.test_post_detail_api`
- `cd frontend && CI=true npm test -- --watchAll=false --runInBand --testPathPattern=post_detail_page.test.tsx`
