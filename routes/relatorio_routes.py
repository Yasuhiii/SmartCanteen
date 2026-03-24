from flask import Blueprint, render_template
from database.connection import get_connection

relatorio_bp = Blueprint("relatorio", __name__)

@relatorio_bp.route("/relatorios")
def relatorios():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT r.nome, SUM(c.quantidade) as total
        FROM compra c
        JOIN refeicao r ON r.id = c.id_refeicao
        GROUP BY r.nome
        ORDER BY total DESC
    """)

    dados = cursor.fetchall()
    conn.close()

    return render_template("relatorios.html", dados=dados)