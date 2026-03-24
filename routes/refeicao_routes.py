from flask import Blueprint, render_template
from models.refeicao import listar_refeicoes

refeicao_bp = Blueprint("refeicao", __name__)

@refeicao_bp.route("/refeicoes")
def refeicoes():
    dados = listar_refeicoes()
    return render_template("refeicoes.html", refeicoes=dados)