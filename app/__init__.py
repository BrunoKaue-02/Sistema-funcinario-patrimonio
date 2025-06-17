from flask import Flask
from app.database.db import db
import os 
from dotenv import load_dotenv

def create_app():
    app = Flask(__name__)

    load_dotenv()

    URL = os.getenv('DATABASE_URL');

    # Configuração do banco 
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # inicializando o SQlAchemy com o app
    db.init_app(app)

    # Importação das model
    from app.models import Funcionario

    # Importação e registro das rotas
    from app.routes.home_routes import home_bp
    from app.routes.funcionario_routes import funcionario_bp
    app.register_blueprint(home_bp)
    app.register_blueprint(funcionario_bp)

    return app