from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

@app.errorhandler(404)
def not_found(error):
      return render_template('404.html'), 404

from package.controllers import pkg
app.register_blueprint(pkg)
db.create_all()


# TEMPORARY FOR TESTING
from package.models import Package
p = Package(name='blah')
db.session.add(p)
db.session.commit()

