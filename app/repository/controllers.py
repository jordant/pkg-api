from app import db
from app import app
from flask.ext.restless import APIManager
from app.repository.models import Repository

manager = APIManager(app, flask_sqlalchemy_db=db)
manager.create_api(Repository, methods=['GET', 'POST', 'DELETE'], results_per_page=-1)
