from inventory import display_inventory, add_product
from transactions import process_sale, view_sales
from auth import login

def show_menu():
    print("\n=== Grocery Management System ===")
    print("1. View Inventory")
    print("2. Add Product")
    print("3. Make Sale")
    print("4. View Sales Report")
    print("5. Exit")

def main():
    if not login():
        return

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            display_inventory()
        elif choice == "2":
            add_product()
        elif choice == "3":
            process_sale()
        elif choice == "4":
            view_sales()
        elif choice == "5":
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
