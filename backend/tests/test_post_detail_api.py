from django.test import TestCase
from rest_framework.test import APIClient

from post.models import Post
from user.models import User
from utils.jwt import generate_jwt


class PostDetailApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
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

    def auth(self):
        token = generate_jwt({"user_id": self.user.id})
        self.client.credentials(HTTP_AUTHORIZATION=token)

    def test_get_post_detail_returns_200(self):
        self.auth()
        response = self.client.get(f"/api/v1/post/{self.post.id}")

        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertEqual(payload["id"], self.post.id)
        self.assertEqual(payload["title"], "Hello")
        self.assertIn("reply", payload)

    def test_get_post_detail_returns_404_for_missing_post(self):
        self.auth()
        response = self.client.get("/api/v1/post/999999")

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()["message"], "not found")

    def test_get_post_detail_requires_auth(self):
        response = self.client.get(f"/api/v1/post/{self.post.id}")

        self.assertEqual(response.status_code, 401)
