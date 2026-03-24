from database.connection import get_connection

def realizar_compra(id_utilizador, id_refeicao, quantidade):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    # 1️⃣ Buscar saldo do utilizador
    cursor.execute("SELECT saldo FROM utilizador WHERE id = %s", (id_utilizador,))
    user = cursor.fetchone()

    # 2️⃣ Buscar preço da refeição
    cursor.execute("SELECT preco FROM refeicao WHERE id = %s", (id_refeicao,))
    refeicao = cursor.fetchone()

    total = refeicao["preco"] * quantidade

    # 3️⃣ Verificar saldo suficiente
    if user["saldo"] < total:
        return False  # saldo insuficiente

    # 4️⃣ Inserir compra
    cursor.execute("""
        INSERT INTO compra (id_utilizador, id_refeicao, quantidade)
        VALUES (%s, %s, %s)
    """, (id_utilizador, id_refeicao, quantidade))

    # 5️⃣ Atualizar saldo
    cursor.execute("""
        UPDATE utilizador
        SET saldo = saldo - %s
        WHERE id = %s
    """, (total, id_utilizador))

    conn.commit()
    conn.close()

    return True