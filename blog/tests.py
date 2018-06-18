import unittest, datetime
from django.test import TestCase
from django.utils import timezone
from .models import Post, Category, Comment, Contact


class Collection(TestCase):
    def text_index(self):
        r = self.client.get('/')
        self.assertEqual(r.status_code, 200)


if __name__ == '__main__':
    unittest.main()


class PostModelTests(TestCase):
    def test_post_creation(self):
        post = Post.objects.create(
            author=laurenhe,
            title="Hello",
            slug="hello",
            created_date=timezone.now() + datetime.timedelta(days=30),
            pics_url="/static/photos/hello.jpg"
        )
        self.assertLess(post.created_date, timezone.now)


class PostDetailViewTestCase(TestCase):

    def setUp(self):
        self.post = Post.objects.create(
            uthor=laurenhe,
            title="Hello",
            slug="hello",
            created_date=timezone.now() + datetime.timedelta(days=30),
            pics_url="/static/photos/hello.jpg"
        )

        def test_post_detail_view(self):
            resp = self.client.get(reverse('post_detail',
                                            kwargs={'pk': self.course.pk}))
            self.assertEqual(resp.status_code, 200)
            self.assertEqual(self.post, resp.context['post'])
            self.assertTemplateUsed(resp, 'blog/post_detail.html')
