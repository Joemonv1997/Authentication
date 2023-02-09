from flask import Flask
from User.models import engine,Base

def manage_app():
    app=Flask(__name__)
    Base.metadata.create_all(bind=engine)
    from User.api import api_method
    app.register_blueprint(api_method,url_prefix="/")
    return app