from flask_mongoengine import MongoEngine

db = MongoEngine()

class Comment(db.Document):
    author = db.StringField(required=True)
    comment = db.StringField(required=True)
    likes = db.IntField(required=True)
    timestamp = db.StringField(required=True)
    user = db.StringField(required=True)
    whoLiked = db.ListField(db.StringField(), required=True)
    postRef = db.ReferenceField('Post')

    def __repr__(self):
        return f"<Comment {self.comment}>"