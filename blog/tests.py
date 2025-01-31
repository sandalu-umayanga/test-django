from django.test import TestCase
from .models import Post

class ModelTesting(TestCase):

    def setUp(self):
        self.blog = Post.objects.create(title='django', author='django', slug='django')

    def test_post_model(self):
        d = self.blog
        self.assertTrue(isinstance(d, Post))
        self.assertEqual(str(d), 'django')

    def test_addition(self):
        self.assertEqual(1 + 1, 3)
        self.assertEqual(2 + 2, 4)
        self.assertEqual(3 + 3, 6)

    def test_subtraction(self):
        self.assertEqual(5 - 3, 2)
        self.assertEqual(10 - 5, 5)
        self.assertEqual(20 - 10, 10)

    def test_multiplication(self):
        self.assertEqual(2 * 3, 6)
        self.assertEqual(4 * 5, 20)
        self.assertEqual(6 * 7, 42)

    def test_division(self):
        self.assertEqual(10 / 2, 5)
        self.assertEqual(20 / 4, 5)
        self.assertEqual(9 / 3, 3)