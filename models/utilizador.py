from database.connection import get_connection
import bcrypt

def criar_utilizador(tipo, nome, numero, curso_dep, email, password):
    conn = get_connection()
    cursor = conn.cursor()

    senha_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    cursor.execute("""
        INSERT INTO utilizador (tipo, nome, numero, curso_departamento, email, password)
        VALUES (%s,%s,%s,%s,%s,%s)
    """, (tipo, nome, numero, curso_dep, email, senha_hash))

    conn.commit()
    conn.close()


def autenticar(numero, password):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM utilizador WHERE numero=%s", (numero,))
    user = cursor.fetchone()

    conn.close()

    if user and bcrypt.checkpw(password.encode(), user["password"].encode()):
        return user

    return None