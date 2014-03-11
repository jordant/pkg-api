from app import db
from app import app
from flask.ext.restless import APIManager
from app.repository_package.models import RepositoryPackage

manager = APIManager(app, flask_sqlalchemy_db=db)
manager.create_api(RepositoryPackage, methods=['GET', 'POST', 'DELETE'], results_per_page=-1)
