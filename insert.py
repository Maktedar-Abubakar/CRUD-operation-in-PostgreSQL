
# Insert Values Function in Postgres:-
from test import get_connection


def insert_record():
    conn = get_connection()
    cur = conn.cursor()
    product_id = int(input("Enter product ID (integer): "))
    name = input("Enter product name (string): ")
    quantity_in_stock = int(input("Enter quantity in stock (integer): "))
    unit_price = float(input("Enter unit price (floating-point number): "))

    cur = conn.cursor()
    insert_query = "INSERT INTO products (product_id, name, quantity_in_stock, unit_price) VALUES (%s, %s, %s, %s);"
    cur.execute(insert_query, (product_id, name,
                quantity_in_stock, unit_price))
    conn.commit()
