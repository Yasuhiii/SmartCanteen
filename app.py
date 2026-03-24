from flask import Flask
from routes.auth_routes import auth_bp
from routes.refeicao_routes import refeicao_bp
from routes.relatorio_routes import relatorio_bp

app = Flask(__name__)
app.secret_key = "smartcanteen_secret"

app.register_blueprint(auth_bp)
app.register_blueprint(refeicao_bp)
app.register_blueprint(relatorio_bp)

if __name__ == "__main__":
    app.run(debug=True)