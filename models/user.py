from flask_mongoengine import MongoEngine

db = MongoEngine()

class User(db.Document):
    email = db.StringField(required=True)
    comments = db.ListField(db.ReferenceField('Comment'))
    firstName = db.StringField(required=True)
    img = db.StringField()
    joined = db.StringField(required=True)
    lastName = db.StringField(required=True)
    location = db.StringField()
    password = db.StringField(required=True)
    popularity = db.IntField(required=True)
    posts = db.ListField(db.ReferenceField('Post'))
    role = db.StringField(required=True)

    def __repr__(self):
        return f"<User {self.email}>"