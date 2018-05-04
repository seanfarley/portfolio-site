from django.test import TestCase


class Collection(TestCase):
    def text_index(self):
        r = self.client.get('/')
        self.assertEqual(r.status_code, 200)
