import sqlite3


def limpar_usuarios():
    conn = sqlite3.connect("usuarios.db", detect_types=sqlite3.PARSE_DECLTYPES)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM usuarios")

    conn.commit()
    conn.close()

    print("Todos os dados foram removidos com sucesso!")


if __name__ == "__main__":
    limpar_usuarios()
