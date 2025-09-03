from test import get_connection


def read_product():
    conn = get_connection()
    if conn is not None:
        cur = conn.cursor()
        table_name = 'products'
        cur.execute(f"SELECT * FROM {table_name};")
        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.close()
        conn.close()
    else:
        print("Connection to database failed.")
