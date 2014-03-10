from app import db

class Package(db.Model):
        __tablename__ = 'package'
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(64), unique=False)
#            description = db.Column(db.String(1024), unique=False)
#            version = db.Column(db.String(64), unique=False)
#            location = db.Column(db.VARCHAR(2083), unique=False)
#            type = db.Column(db.Enum("debian", "rpm"))
#            arch = db.Column(db.Enum("amd64", "i386"))
#            created = db.Column(db.DATETIME, unique=False)
#            public = db.Column(db.Enum("True", "False"), unique=False, default="True")


#def __init__(self, id=None, name=None, description=None, version=None, location=None, type=None, arch=None, created=None, public=None):
def __init__(self, name=None):
        self.name = name

def __repr__(self):
        return '<Package %r>' % (self.name) 
