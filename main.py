from insert import insert_record
from read import read_product
from update import update_product
from delete import delete_product


def main():
    while True:
        print("\n----- Product Database Menu -----")
        print("1. Create (Insert)")
        print("2. Read (Select)")
        print("3. Update")
        print("4. Delete")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            insert_record()
        elif choice == "2":
            read_product()
        elif choice == "3":
            update_product()
        elif choice == "4":
            delete_product()
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
