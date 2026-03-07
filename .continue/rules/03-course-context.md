当前课程主题是：恢复并完善“帖子详情”功能。

本课程包含六个任务：

1. 实现后端帖子详情接口
2. 完成前端帖子详情页加载
3. 完成前后端联调
4. 编写后端单元测试
5. 编写 API 测试
6. 配置 GitHub Actions CI

当前项目中的关键链路是：

浏览器路由：
- /post/:postId

前端页面：
- frontend/src/post/post_detail_page.tsx

前端 API 封装：
- frontend/src/backend.tsx 中的 post(postId)

后端 API 路由：
- backend/post/urls.py
- api/v1/post/<int:postId>

后端视图：
- backend/post/views.py 中的 PostDetailView.get()

后端业务查询：
- backend/post/controllers.py 中的 get_post_detail(post_id)

测试与验证：
- backend/tests/test_post_detail.py
- backend/tests/test_post_detail_api.py
- frontend/src/post/post_detail_page.test.tsx
- .github/workflows/ci.yml
- tools/checks/check_post_detail.py
- Makefile

默认推荐顺序：
1 -> 2 -> 3 -> 4 -> 5 -> 6

允许顺序：
1 -> 4 -> 5 -> 2 -> 3 -> 6

如果学生没有明确说明任务，默认优先推进当前最靠前、最基础、最应该先完成的任务。
