import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api

from resources.task_resource import TaskResource
from resources.user_resource import UserResource
from resources.project_resource import ProjectResource
from resources.user_task_resource import UserTaskResource
from models import db
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
CORS(app, supports_credentials=True)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
api = Api(app)
migrate = Migrate(app, db)


api.add_resource(TaskResource, '/task', '/task/<int:task_id>')
api.add_resource(UserResource, '/user', '/user/<int:user_id>')
api.add_resource(ProjectResource, '/project', '/project/<int:project_id>')
api.add_resource(UserTaskResource, '/user_task', '/user_task/<int:user_task_id>')

if __name__ == '__main__':
    app.run(debug=True)