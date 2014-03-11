from app import db

class Base(db.Model):
        __abstract__  = True
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(64), unique=False)
        created  = db.Column(db.DateTime,  default=db.func.current_timestamp())
        modified = db.Column(db.DateTime,  default=db.func.current_timestamp())

class Repository(Base):
        __tablename__ = 'repository'
        description = db.Column(db.String(1024), unique=False)
        type = db.Column(db.Enum("debian", "rpm"))
        release = db.Column(db.String(64), unique=False)
        public = db.Column(db.Enum("True", "False"), unique=False, default="True")
        repository_package = db.relationship('RepositoryPackage')

        def __init__(self, name=None, description=None, type=None, release=None, public=True):
                self.name = name
                self.description = description
                self.type = type
                self.release = release
                self.public = public

        def __repr__(self):
                return '<Repository %r>' % (self.name) 
