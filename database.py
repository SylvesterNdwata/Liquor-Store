import sqlite3 as sql
import pandas as pd

class Database:
    def __init__(self, db_name):
        self.con = sql.connect(db_name)
        self.cur = self.con.cursor()
        
    
    def create_tables(self):
        self.cur.execute("CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, name TEXT, category TEXT, price REAL)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS sales (id INTEGER PRIMARY KEY, product_id INTEGER, quantity INTEGER, sale_date TEXT, FOREIGN KEY(product_id) REFERENCES products(id))")
        self.con.commit()
        
    def insert_product(self, name, category, price):
        self.cur.execute("INSERT INTO products (name, category, price) VALUES (?, ?, ?)", (name, category, price))
        self.con.commit()
    
    def insert_sale(self, product_id, quantity, sale_date):
        self.cur.execute("INSERT INTO sales (product_id, quantity, sale_date) VALUES (?, ?, ?)", (product_id, quantity, sale_date))
        self.con.commit()
        
    def fetch_products(self):
        self.res = self.cur.execute("SELECT * FROM products")
        data = self.res.fetchall()
        return pd.DataFrame(data, columns=['id', 'name', 'category', 'price'])
        self.con.commit()
    
    def fetch_sales(self):
        self.res = self.cur.execute("SELECT * FROM sales")
        data = self.res.fetchall()
        return pd.DataFrame(data, columns=['id', 'product_id', 'quantity', 'sale_date'])
        self.con.commit()