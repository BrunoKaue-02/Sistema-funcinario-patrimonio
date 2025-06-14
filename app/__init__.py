from flask import Flask

app = Flask(__name__)

def create_app():
    app = Flask(__name__)

    from app.routes.home_routes import home_bp
    
    app.register_blueprint(home_bp)

    return app