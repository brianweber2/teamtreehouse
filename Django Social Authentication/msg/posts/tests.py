from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase

from . import models


class PostTestCaseBase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="kennethlove")


class PostModel(PostTestCaseBase):
    def test_markdown(self):
        post = models.Post.objects.create(
            user=self.user,
            message="This post should have\n\ntwo paragraphs"
        )
        self.assertInHTML("<p>two paragraphs</p>", post.message_html)

    def test_url(self):
        post = models.Post.objects.create(
            user=self.user,
            message="This message should have a URL"
        )
        self.assertEqual(
            post.get_absolute_url(),
            reverse('posts:single', kwargs={
                "username": self.user.username,
                "pk": post.pk
            })
        )


class PostPublicViews(PostTestCaseBase):
    def setUp(self):
        super().setUp()
        for msg in ["one", "two", "three", "four", "five"]:
            models.Post.objects.create(user=self.user, message=msg)
        self.messages = models.Post.objects.all()

    def test_all_list(self):
        resp = self.client.get(reverse("posts:all"))
        self.assertQuerysetEqual(
            self.messages,
            resp.context_data['object_list'],
            transform=lambda x: x  # Don't transform either queryset
        )

    def test_user_list(self):
        user2 = User.objects.create(username="testuser")
        msg = models.Post.objects.create(user=user2, message="Not by Kenneth")
        resp = self.client.get(
            reverse("posts:for_user", kwargs={"username": self.user.username})
        )
        self.assertNotIn(msg, resp.context_data["object_list"])

    def test_single(self):
        resp = self.client.get(
            reverse("posts:single", kwargs={
                "username": self.user.username,
                "pk": self.messages[0].pk
            })
        )
        self.assertEqual(self.messages[0], resp.context_data["object"])


class PostPrivateViews(PostTestCaseBase):
    def test_create_with_login(self):
        self.client.force_login(self.user)
        resp = self.client.post(
            reverse("posts:create"),
            data={"message": "New message"},
            follow=True
        )
        self.assertEqual(models.Post.objects.count(), 1)
        self.assertEqual(resp.status_code, 200)

    def test_create_requires_login(self):
        resp = self.client.get(reverse("posts:create"))
        self.assertNotEqual(resp.status_code, 200)

    def test_delete_own_post_with_login(self):
        post = models.Post.objects.create(
            user=self.user,
            message="Time is short"
        )
        self.client.force_login(self.user)
        url = reverse("posts:delete", kwargs={"pk": post.pk})
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(post, resp.context_data["object"])

        resp2 = self.client.post(url, follow=True)
        self.assertEqual(resp2.status_code, 200)
        self.assertEqual(models.Post.objects.count(), 0)

    def test_delete_others_post_with_login(self):
        user2 = User.objects.create(username="testuser")
        post = models.Post.objects.create(
            user=user2,
            message="Time is short"
        )
        self.client.force_login(self.user)
        url = reverse("posts:delete", kwargs={"pk": post.pk})
        resp = self.client.get(url)
        self.assertNotEqual(resp.status_code, 200)

        resp2 = self.client.post(url, follow=True)
        self.assertNotEqual(resp2.status_code, 200)
        self.assertEqual(models.Post.objects.count(), 1)

    def test_delete_post_without_login(self):
        self.client.logout()
        post = models.Post.objects.create(
            user=self.user,
            message="Time is short"
        )
        url = reverse("posts:delete", kwargs={"pk": post.pk})
        resp = self.client.get(url)
        self.assertNotEqual(resp.status_code, 200)

        resp2 = self.client.post(url, follow=True)
        self.assertNotEqual(resp2.status_code, 200)
        self.assertEqual(models.Post.objects.count(), 1)
