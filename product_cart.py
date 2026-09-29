products={101:{"name":"Rice 5kg","category":"Grocery","price":350,"stock":20},
102:{"name":"Wheat Flour 5kg","category":"Grocery","price":280,"stock":18},
103:{"name":"Cooking Oil 1L","category":"Grocery","price":145,"stock":25},
104:{"name":"Milk 1L","category":"Dairy","price":65,"stock":30},
105:{"name":"Biscuits","category":"Snacks","price":40,"stock":35},
106:{"name":"Soap","category":"Personal Care","price":55,"stock":25},
107:{"name":"Shampoo","category":"Personal Care","price":180,"stock":15},
108:{"name":"Toothpaste","category":"Personal Care","price":95,"stock":20}}

cart={}

def display_products():
    print("\nProduct ID | Product | Category | Price | Stock")
    for pid,p in products.items():
        print(pid,"|",p["name"],"|",p["category"],"| ₹",p["price"],"|",p["stock"])

def search_product():
    keyword=input("Enter product name: ").lower()
    found=False
    for pid,p in products.items():
        if keyword in p["name"].lower():
            print(pid,p["name"],p["category"],"₹",p["price"],"Stock:",p["stock"])
            found=True
    if not found:
        print("Product not found.")

def add_to_cart():
    try:
        pid=int(input("Enter product ID: "))
        if pid not in products:
            print("Invalid product ID.")
            return
        qty=int(input("Enter quantity: "))
        if qty<=0:
            print("Quantity must be positive.")
        elif qty>products[pid]["stock"]:
            print("Not enough stock.")
        else:
            cart[pid]=cart.get(pid,0)+qty
            print("Product added to cart.")
    except ValueError:
        print("Enter valid numbers.")

def view_cart():
    if not cart:
        print("Cart is empty.")
        return
    print("\nCart")
    total=0
    for pid,qty in cart.items():
        p=products[pid]
        amount=p["price"]*qty
        total+=amount
        print(p["name"],"x",qty,"= ₹",amount)
    print("Subtotal: ₹",total)

def remove_from_cart():
    if not cart:
        print("Cart is empty.")
        return
    try:
        pid=int(input("Enter product ID to remove: "))
        if pid in cart:
            del cart[pid]
            print("Product removed.")
        else:
            print("Product not found in cart.")
    except ValueError:
        print("Enter a valid product ID.")