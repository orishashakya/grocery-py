from storage import load_data, save_data

INVENTORY_FILE = "data/inventory.json"

def display_inventory():
    inventory = load_data(INVENTORY_FILE)
    if not inventory:
        print("\nInventory is empty.")
        return

    print("\n--- Available Products ---")
    print("ID\tName\tPrice\tQuantity")
    for pid, item in inventory.items():
        print(f"{pid}\t{item['name']}\t{item['price']}\t{item['quantity']}")

def add_product():
    inventory = load_data(INVENTORY_FILE)

    product_id = input("Enter product ID: ")
    if product_id in inventory:
        print("Product ID already exists.")
        return

    name = input("Enter product name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    inventory[product_id] = {
        "name": name,
        "price": price,
        "quantity": quantity
    }

    save_data(INVENTORY_FILE, inventory)
    print("Product added successfully.")
