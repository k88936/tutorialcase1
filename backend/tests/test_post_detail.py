from datetime import timedelta

from django.test import TestCase
from django.utils import timezone

from post.controllers import get_post_detail
from post.models import Post, Reply
from user.models import User


class PostDetailControllerTests(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="alice",
            password="123456",
            nickname="Alice",
            mobile="+86.123456789012",
            magic_number=7,
            url="https://example.com",
        )
        self.post = Post.objects.create(
            user=self.user,
            title="Hello",
            content="World",
            last_replied_user=self.user,
        )

    def test_get_post_detail_success(self):
        detail, result = get_post_detail(self.post.id)

        self.assertEqual(result, "ok")
        self.assertEqual(detail["id"], self.post.id)
        self.assertEqual(detail["title"], "Hello")
        self.assertEqual(detail["content"], "World")
        self.assertEqual(detail["userId"], self.user.id)
        self.assertEqual(detail["nickname"], "Alice")
        self.assertIn("reply", detail)
        self.assertEqual(detail["reply"], [])

    def test_get_post_detail_not_found(self):
        detail, result = get_post_detail(999999)

        self.assertIsNone(detail)
        self.assertEqual(result, "not_found")

    def test_reply_order_and_root_reply_id(self):
        root_early = Reply.objects.create(
            user=self.user,
            post=self.post,
            content="root early",
            reply=None,
        )
        child = Reply.objects.create(
            user=self.user,
            post=self.post,
            content="child",
            reply=root_early,
        )
        root_late = Reply.objects.create(
            user=self.user,
            post=self.post,
            content="root late",
            reply=None,
        )

        now = timezone.now()
        Reply.objects.filter(id=root_early.id).update(
            created=now - timedelta(minutes=3), updated=now - timedelta(minutes=3)
        )
        Reply.objects.filter(id=child.id).update(
            created=now - timedelta(minutes=2), updated=now - timedelta(minutes=2)
        )
        Reply.objects.filter(id=root_late.id).update(
            created=now - timedelta(minutes=1), updated=now - timedelta(minutes=1)
        )

        detail, result = get_post_detail(self.post.id)

        self.assertEqual(result, "ok")
        self.assertEqual(
            [reply["id"] for reply in detail["reply"]],
            [root_early.id, child.id, root_late.id],
        )
        reply_map = {reply["id"]: reply for reply in detail["reply"]}
        self.assertEqual(reply_map[root_early.id]["replyId"], 0)
        self.assertEqual(reply_map[root_late.id]["replyId"], 0)
        self.assertEqual(reply_map[child.id]["replyId"], root_early.id)
