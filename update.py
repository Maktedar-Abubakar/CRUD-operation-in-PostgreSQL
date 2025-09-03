from test import get_connection


def update_product():
    conn = get_connection()
    if conn is not None:
        cur = conn.cursor()

        old_product_id = input("Enter current product_id: ")
        old_name = input("Enter current name: ")
        old_quantity_in_stock = input("Enter current quantity_in_stock: ")
        old_unit_price = input("Enter current unit_price: ")

        new_product_id = input("Enter new product_id: ")
        new_name = input("Enter new name: ")
        new_quantity_in_stock = input("Enter new quantity_in_stock: ")
        new_unit_price = input("Enter new unit_price: ")

        update_query = """
        UPDATE products
        SET product_id = %s, name = %s, quantity_in_stock = %s, unit_price = %s
        WHERE product_id = %s AND name = %s AND quantity_in_stock = %s AND unit_price = %s;
        """

        cur.execute(
            update_query,
            (
                new_product_id,
                new_name,
                new_quantity_in_stock,
                new_unit_price,
                old_product_id,
                old_name,
                old_quantity_in_stock,
                old_unit_price
            )
        )
        conn.commit()
        print("Row updated successfully!")
        cur.close()
        conn.close()
    else:
        print("Connection to database failed.")
