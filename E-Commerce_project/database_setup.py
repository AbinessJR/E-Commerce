import sqlite3

# Create a SQLite database and connect to it
conn = sqlite3.connect('ecommerce.db')
cursor = conn.cursor()

# Create tables for Sales, Customers, Products, Orders, etc.
cursor.execute('''
    CREATE TABLE Sales (
        sale_id INTEGER PRIMARY KEY,
        product_id INTEGER,
        customer_id INTEGER,
        sale_date DATE,
        sale_amount REAL
    )
''')

# Create tables for Customers, Products, and Orders (similar CREATE TABLE statements)

# Insert sample data (you can automate this with data import scripts)
cursor.execute("INSERT INTO Sales (product_id, customer_id, sale_date, sale_amount) VALUES (?, ?, ?, ?)",
               (1, 1, '2023-09-25', 100.0))

# Commit changes and close the database connection
conn.commit()
conn.close()
