from flask import Flask
from flask_cors import CORS
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'common'))

from User.models import engine,Base
def manage_app():
    app=Flask(__name__)
    Base.metadata.create_all(bind=engine)
    from User.api import api_method
    app.register_blueprint(api_method,url_prefix="/")
    CORS(app)
    return app