from test import get_connection


def delete_product():
    conn = get_connection()
    if conn is not None:
        cur = conn.cursor()

        column_name = input("Enter the column name to delete by: ")
        value_to_delete = input(
            f"Enter the value for {column_name} to delete: ")

        # Build the query safely.
        delete_query = f"DELETE FROM products WHERE {column_name} = %s;"
        cur.execute(delete_query, (value_to_delete,))

        conn.commit()
        print("Row deleted successfully!")

        cur.close()
        conn.close()
    else:
        print("Connection to database failed.")
