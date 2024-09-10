from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime, date

app = Flask(__name__)


def adapt_date_iso(val):
    """Adaptador para converter datetime.date para string ISO."""
    return val.isoformat()


def convert_date_iso(val):
    """Conversor para converter string ISO para datetime.date."""
    return datetime.strptime(val.decode(), "%Y-%m-%d").date()


sqlite3.register_adapter(date, adapt_date_iso)
sqlite3.register_converter("DATE", convert_date_iso)


@app.route("/api/usuarios", methods=["POST"])
def save_usuarios():
    data = request.json
    conn = sqlite3.connect("usuarios.db", detect_types=sqlite3.PARSE_DECLTYPES)
    cursor = conn.cursor()

    # Criar tabela
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        idade INTEGER,
        email TEXT,
        telefone TEXT,
        endereco TEXT,
        data_cadastro DATE,
        ativo BOOLEAN,
        salario REAL
    )
    """
    )

    cursor.execute("DELETE FROM usuarios")

    for user in data:
        cursor.execute(
            """
        INSERT INTO usuarios (id, nome, idade, email, telefone, endereco, data_cadastro, ativo, salario)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
            (
                user["id"],
                user["nome"],
                user["idade"],
                user["email"],
                user["telefone"],
                user["endereco"],
                user["data_cadastro"],
                user["ativo"],
                user["salario"],
            ),
        )

    conn.commit()
    conn.close()

    return jsonify({"message": "Dados salvos com sucesso!"}), 200


@app.route("/api/usuarios", methods=["GET"])
def get_usuarios():
    conn = sqlite3.connect("usuarios.db", detect_types=sqlite3.PARSE_DECLTYPES)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM usuarios")
    rows = cursor.fetchall()

    usuarios = []
    for row in rows:
        usuarios.append(
            {
                "id": row[0],
                "nome": row[1],
                "idade": row[2],
                "email": row[3],
                "telefone": row[4],
                "endereco": row[5],
                "data_cadastro": row[6],
                "ativo": row[7],
                "salario": row[8],
            }
        )

    conn.close()
    return jsonify(usuarios), 200


if __name__ == "__main__":
    app.run(debug=True)
