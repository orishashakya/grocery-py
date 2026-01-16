from datetime import datetime
from storage import load_data, save_data

INVENTORY_FILE = "data/inventory.json"
SALES_FILE = "data/sales.json"

def process_sale():
    inventory = load_data(INVENTORY_FILE)
    sales = load_data(SALES_FILE)

    product_id = input("Enter product ID: ")
    quantity = int(input("Enter quantity: "))

    if product_id not in inventory:
        print("Product not found.")
        return

    product = inventory[product_id]

    if quantity > product["quantity"]:
        print("Not enough stock available.")
        return

    total_price = quantity * product["price"]
    product["quantity"] -= quantity

    sale_record = {
        "product_id": product_id,
        "name": product["name"],
        "quantity": quantity,
        "total": total_price,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    sales.append(sale_record)

    save_data(INVENTORY_FILE, inventory)
    save_data(SALES_FILE, sales)

    print(f"Sale completed. Total bill: Rs {total_price}")

def view_sales():
    sales = load_data(SALES_FILE)
    if not sales:
        print("\nNo sales recorded yet.")
        return

    total_sales = 0
    print("\n--- Sales Records ---")
    print("Date\t\tProduct\tQty\tTotal")
    for s in sales:
        print(f"{s['timestamp']}\t{s['name']}\t{s['quantity']}\t{s['total']}")
        total_sales += s['total']

    print(f"\nTotal Revenue: Rs {total_sales}")
