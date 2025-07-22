from post import Post


class Blog:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.posts = []

    def __repr__(self):
        # post_count = len(self.posts)
        # post_word = "Post" if post_count == 1 else "Posts"
        return f"{self.title} by {self.author} has {len(self.posts)} Post{'s' if len(self.posts) != 1 else ''}"


    def create_post(self, title, content):
        self.posts.append(Post(title, content))

    def json(self):
        return {

            "title": self.title,
            "author": self.author,
            "posts": [post.json() for post in self.posts]
        }
