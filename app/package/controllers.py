from flask import Blueprint, jsonify
from app import db
from app.package.models import Package
from flask.ext.sqlalchemy import SQLAlchemy

pkg = Blueprint('package', __name__, url_prefix='/package')

@pkg.route('/<package_id>', methods = ['GET'])
def package(package_id):
        package = Package.query.filter_by(id=package_id)
        print package
        return ("Package id %r" % package_id)
#        return jsonify( { 'packages': package } )
