from psycopg2 import connect


def get_connection():
    try:
        conn = connect(
            dbname="postgres",
            user="postgres",
            password="password",
            host="localhost",
            port="5432"
        )
        return conn
    except Exception as e:
        print("Error connecting to PostgreSQL:", e)
        return None
