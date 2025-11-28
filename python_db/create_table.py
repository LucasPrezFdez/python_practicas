from connect import get_connection


def crate_table():
    query = """
    CREATE TABLE IF NOT EXISTS profesores(
        id SERIAL PRIMARY KEY,
        name VARCHAR(100)
    )
    """

    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
    finally:
        conn.close()


if __name__ == "__main__":
    crate_table()
