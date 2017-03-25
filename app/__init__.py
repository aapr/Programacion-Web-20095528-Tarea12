from flask import Flask
from app.models import db
from app.review.controllers import review
from app.config import Config

app = Flask(__name__)

app.config.from_object(Config)
db.init_app(app)
db.create_all(app=app)

app.register_blueprint(review, url_prefix='/review')