from flask_mongoengine import MongoEngine

db = MongoEngine()

class Post(db.Document):
    author = db.ReferenceField('User', required=True)
    body = db.StringField(required=True)
    comments = db.ListField(db.ReferenceField('Comment'))
    favorites = db.IntField(required=True)
    likes = db.IntField(required=True)
    tags = db.ListField(db.StringField())
    timestamp = db.StringField(required=True)
    title = db.StringField(required=True)
    whoLiked = db.ListField(db.StringField(), required=True)
    views = db.IntField(required=True)

    def __repr__(self):
        return f"<Post {self.title}>"