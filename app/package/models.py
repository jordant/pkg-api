from app import db

class Base(db.Model):
        __abstract__  = True
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(64), unique=False)
        created  = db.Column(db.DateTime,  default=db.func.current_timestamp())
        modified = db.Column(db.DateTime,  default=db.func.current_timestamp())

class Package(Base):
        __tablename__ = 'package'
        description = db.Column(db.String(1024), unique=False)
        version = db.Column(db.String(64), unique=False)
        location = db.Column(db.VARCHAR(2083), unique=False)
        md5sum = db.Column(db.VARCHAR(32), unique=False)
        type = db.Column(db.Enum("debian", "rpm"))
        arch = db.Column(db.Enum("amd64", "i386"))
        public = db.Column(db.Enum("True", "False"), unique=False, default="True")

        def __init__(self, name=None, description=None, version=None, location=None, md5sum=None, type=None, arch=None, public=True):
                self.name = name
                self.location = location
                self.description = description
                self.version = version
                self.md5sum = md5sum
                self.type = type
                self.arch = arch
                self.public = public

        def __repr__(self):
                return '<Package %r>' % (self.name) 

        #@property
#        def serialize(self):
#                return {
#                        'id': self.id,
#                        'name': self.name,
#                        'created': self.created,
#                        'modified': self.modified,
#                        'description': self.description,
#                        'version': self.version,
#                        'location': self.location,
#                        'md5sum': self.md5sum,
#                        'type': self.type,
#                        'arch': self.arch,
#                        'public': self.public
#                        }
