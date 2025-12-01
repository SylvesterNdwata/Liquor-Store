from database import Database
from invoice import Invoice
import pandas as pd
from datetime import datetime

database = Database('LiquorStore.db')

database.customer_table()

print("Welcome to the Liquor Store")

invoce = Invoice()

customer_invoice = invoce.items

database.customer_name = input("Please enter your name: ").title()

customer_age = int(input("Please input your age: "))

x = datetime.now()
date = x.strftime("%x")

if customer_age < 18:
    print("You are not liable to purchase our products, must be 18 or older")
    exit()
elif customer_age >= 18:
 print(f"Hello, {database.customer_name}! Here are our available products:")

print(database.fetch_products())

cart = {}

shop = True
while shop:
    product_name = input("Please enter the name of the product you wish to purchase: ").title()
    product_quantity = int(input(f"How many units of {product_name} would you like to buy? "))
    if product_name not in database.fetch_products().name.values:
        print("Sorry, we do not have that product available.")
    elif product_name in database.fetch_products().name.values and customer_age >= 18:
        product = database.fetch_products()[database.fetch_products().name == product_name]
        product_id = product.id.item()
        price = product.price.item()
        print(f"The price of {product_name} is ${price} per unit.")
        customer_invoice.append(product_name)
        invoce.add_item(price * product_quantity)
        if product_name in cart:
            cart[f"{product_name}"] += product_quantity
        elif product_name not in cart:
            cart[f"{product_name}"] = product_quantity
        database.insert_customer(name=database.customer_name, age=customer_age)
        database.insert_sale(product_id=product_id, sale_date=date, quantity=product_quantity)
        print(f"{product_name} has been added to your invoice.")
    add_to_cart = input("Would you like to keep shopping? Yes or No?: ").lower()
    if add_to_cart == "yes":
        shop = True
    elif add_to_cart == "no":
        shop = False
        receipt_rows = []
        products = database.fetch_products()
        for product_name, product_quantity in cart.items():
            product = products[products["name"] == product_name]
            unit_price = product.price.item()
            subtotal = unit_price * product_quantity
            receipt_rows.append((product_name, product_quantity, unit_price, subtotal))
        receipt = pd.DataFrame(receipt_rows, columns=["Product", "Product_quantity", "Unit_price", "Subtotal"])
        total = receipt.Subtotal.sum()
        receipt.loc[len(receipt)] = ["TOTAL", "", "", total]
        receipt.to_csv("receipt.csv", index=False)
        print(receipt)
    else:
        print("Please type Yes or No")
        add_to_cart = input("Would you like to keep shopping? Yes or No?: ").lower()
    
    

        
            


        
            







