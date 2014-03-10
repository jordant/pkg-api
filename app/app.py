from flask import Blueprint, jsonify
from flask.ext.sqlalchemy import SQLAlchemy
#from package import Package

package = Blueprint('package', __name__, url_prefix='/pacakge')

@package.route('/<int:package_id>', methods = ['GET'])

def package(package_id):
        return "package"
