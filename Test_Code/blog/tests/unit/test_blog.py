
from unittest import TestCase
from blog import Blog



class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog("Test", "Test Author")
        self.assertEqual(b.title, "Test")
        self.assertEqual(b.author, "Test Author")
        self.assertListEqual([], b.posts)

    def test_repr(self):
        b = Blog("Test", "Test Author")
        self.assertEqual(b.__repr__(), "Test by Test Author (0 Posts)")

    def test_repr_multiple(self):
        b1 = Blog("Test1", "Test Author1")
        b1.posts = ["test1"]
        b2 = Blog("Test2", "Test Author2")
        b2.posts = ["test1", "test2"]

        self.assertEqual(b1.__repr__(), "Test1 by Test Author1 has 1 Post")
        self.assertEqual(b2.__repr__(), "Test2 by Test Author2 has 2 Posts")