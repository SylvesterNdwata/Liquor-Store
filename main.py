from database import Database
from invoice import Invoice

database = Database('LiquorStore.db')

print("Welcome to the Liquor Store")

invoce = Invoice()

customer_invoice = invoce.items

customer_name = input("Please enter your name: ").title()

customer_age = int(input("Please input your age: "))

if customer_age < 18:
    print("You are not liable to purchase our products, must be 18 or older")
    exit()
elif customer_age >= 18:
 print(f"Hello, {customer_name}! Here are our available products:")

print(database.fetch_products())

product_name = input("Please enter the name of the product you wish to purchase: ").title()

while True:
    if product_name not in database.fetch_products().name.values:
        print("Sorry, we do not have that product available.")
    elif product_name in database.fetch_products().name.values and customer_age >= 18:
        product = database.fetch_products()[database.fetch_products().name == product_name]
        product_id = database.fetch_products()[database.fetch_products().name == product_name].id.item()
        price = product.price.item()
        print(f"The price of {product_name} is ${price} per unit.")
        customer_invoice.append(product_name)
        invoce.add_item(price)
        print(f"{product_name} has been added to your invoice.")
        more_products = input("Would you like to purchase another product? (yes/no): ").lower()
        if more_products == "no":
            print("Thank you for your purchase!")
            print(f"Your invoice items: {customer_invoice}")
            print(f"Total cost: ${invoce.total_cost}")
            break
        elif more_products == "yes":
            product_name = input("Please enter the name of the product you wish to purchase: ").title()
            if product_name not in database.fetch_products().name.values:
                print("Sorry, we do not have that product available.")
            elif product_name in database.fetch_products().name.values:
                product = database.fetch_products()[database.fetch_products().name == product_name]
                product_id = database.fetch_products()[database.fetch_products().name == product_name].id.item()
                price = product.price.item()
                print(f"The price of {product_name} id ${price} per unit.")
                customer_invoice.append(product_name)
                invoce.add_item(price)
                print(f"{product_name} has been added to your invoice.")
            







