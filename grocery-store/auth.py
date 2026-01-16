# auth.py
def login():
    print("\n=== Admin Login ===")
    USERNAME = "admin"
    PASSWORD = "1234"

    username = input("Username: ")
    password = input("Password: ")

    if username == USERNAME and password == PASSWORD:
        print("Login successful!\n")
        return True
    else:
        print("Invalid username or password.\n")
        return False
