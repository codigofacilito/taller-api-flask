from flask import Flask

from .models import db
from .models.task import Task

from .views import api_v1

app = Flask(__name__)

def create_app(enviroment):
    app.config.from_object(enviroment)
    
    app.register_blueprint(api_v1)

    with app.app_context():
        db.init_app(app)
        db.create_all()

    return app