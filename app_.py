from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from models import *
from auth import auth_bp
from content import content_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///streaming_service.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'sua_chave_secreta_aqui'

db = SQLAlchemy(app)
migrate = Migrate(app, db)
CORS(app)

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(content_bp, url_prefix='/content')

if __name__ == '__main__':
    app.run(debug=True)

