from flask import Flask
from app.database.db import db
import os 
from dotenv import load_dotenv

def create_app():
    # Carrega as variáveis de ambiente do arquivo .env
    load_dotenv()

    # Cria uma instância da aplicação Flask
    app = Flask(__name__)

    # Define a chave secreta da aplicação (necessária para sessões, cookies, CSRF, etc)
    app.secret_key = os.getenv('SECRET_KEY')  # Recomendado manter essa chave em segredo no .env

    # Apenas para fins de depuração, imprime a URL do banco no terminal
    print("DATABASE_URL:", os.getenv("DATABASE_URL"))  

    # Configura a string de conexão com o banco de dados
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')

    # Desativa notificações de modificação de objetos (economiza recursos)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializa o SQLAlchemy com a aplicação Flask
    db.init_app(app)

    # Importa o modelo de dados (tabelas) - importante estar após o init_app
    from app.models import Funcionario

    # Importa e registra as rotas (blueprints) da aplicação
    from app.routes.home_routes import home_bp
    from app.routes.funcionario_routes import funcionario_bp
    from app.routes.index_routes import index_bp
    from app.routes.formulario_patrimonio_routes import patrimonio_bp
    from app.routes.patrimonio_routes import homeP_bp
    from app.routes.fabricante_routes import fabricante_bp
    from app.routes.notas_routes import nota_bp
    from app.routes.vendedor_routes import vendedor_bp
    
    app.register_blueprint(home_bp)            
    app.register_blueprint(funcionario_bp)
    app.register_blueprint(patrimonio_bp)
    app.register_blueprint(index_bp) 
    app.register_blueprint(homeP_bp)
    app.register_blueprint(fabricante_bp)
    app.register_blueprint(nota_bp)
    app.register_blueprint(vendedor_bp)

    # Retorna a aplicação configurada
    return app
