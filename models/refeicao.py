from database.connection import get_connection

def listar_refeicoes():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM refeicao")
    dados = cursor.fetchall()

    conn.close()
    return dados


def criar_refeicao(nome, categoria, preco, quantidade):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO refeicao (nome, categoria, preco, quantidade_diaria)
        VALUES (%s,%s,%s,%s)
    """, (nome, categoria, preco, quantidade))

    conn.commit()
    conn.close()