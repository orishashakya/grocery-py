# Grocery Management System

## Overview
This is a **Python-based Grocery Management System** designed to manage inventory and handle basic transactions efficiently. The system is **menu-driven** (command-line interface) and uses JSON files to store inventory and sales data.

This project demonstrates:
- Modular programming in Python
- File-based data handling
- Basic user authentication
- Inventory and transaction management
- Sales reporting

---

## Features
1. **Admin Login**  
   - Username: `admin`  
   - Password: `1234`  

2. **Inventory Management**
   - View existing products
   - Add new products

3. **Transactions**
   - Process sales with quantity and total price
   - Updates inventory automatically

4. **Sales Reports**
   - View all sales records
   - Calculate total revenue

---

## File Structure
grocery-store/
│
├── main.py # Entry point
├── inventory.py # Inventory functions
├── transactions.py # Sales and reports
├── storage.py # JSON file handling
├── auth.py # Login system
├── data/
│ ├── inventory.json # Inventory data
│ └── sales.json # Sales data
└── README.md