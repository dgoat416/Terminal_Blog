__author__ = "DGOAT"

# universally unique identifier (uuid)
import uuid
from database import Database
import datetime

# container to hold things belonging to the same object
# same as normal classes in Java and C++
# we need object param to say that it comes from object
class Post(object):

    # initializer (Constructor)
    # only can have default parameters in a method at the end (last param)
    def __init__(self, blog_id, title, content, author, date = datetime.datetime.utcnow(), id = None):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.created_date = date
        self.id = uuid.uuid4().hex if id is None else id




    def save_to_mongo(self):
        Database.insert(collection = "posts",
                        data = self.json())

# returns a json representation of a "Post" object
    def json(self):
        return {
            "id" : self.id,
            "blog_id" : self.blog_id,
            "author": self.author,
            "content": self.content,
            "title": self.title,
            "date": self.created_date
        }

    @classmethod
    def from_mongo(cls, id):
        post_data = Database.find_one(collection = "posts", query = {"id": id})
        return cls(blog_id=post_data["blog"],
                   title= post_data["title"],
                   content = post_data["content"],
                   author = post_data["author"],
                   created_date = post_data["date"],
                   id=post_data["id"])

    @staticmethod
    def from_blog(id):
        return [ post for post in Database.find(collection = "posts", query = {"blog_id": id})]