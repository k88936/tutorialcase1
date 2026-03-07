# 作业：恢复帖子详情功能

## 目标
你需要恢复并完善论坛系统中的“帖子详情”功能。

## 需要完成
1. 后端实现帖子详情查询逻辑
2. 帖子不存在时返回 404
3. 前端页面根据路由参数加载帖子详情
4. 成功 / 失败 / 加载状态正确显示
5. 补后端 unittest
6. 补前端测试
7. 配置 GitHub Actions

## 重点文件
- backend/post/urls.py
- backend/post/views.py
- backend/post/controllers.py
- frontend/src/post/post_detail_page.tsx

## 建议顺序
1. 先看路由
2. 再补 controller
3. 再补 view
4. 跑后端测试
5. 再补前端 loadPost
6. 跑前端测试
7. 最后看 CI

## 本地检查
- make check
- make backend-test
- make frontend-test
- make test
