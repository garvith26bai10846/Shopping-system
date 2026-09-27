# ==========================================
# SHOPPING AND BILLING SYSTEM
# CSE1021 PROJECT
# ==========================================

from datetime import datetime

# ------------------------------------------
# PRODUCT DETAILS
# ------------------------------------------

products = { 101: {"name":"Rice","category":"Grocery","price":350,"stock":20},
    102: {"name":"Wheat Flour","category":"Grocery","price":280,"stock":18},
    103: {"name":"Cooking Oil","category":"Grocery","price":145,"stock":25},
    104: {"name":"Milk","category":"Dairy","price":65,"stock":30},
    105: {"name":"Biscuits","category":"Snacks","price":40,"stock":35},
    106: {"name":"Soap","category":"Personal Care","price":55,"stock":25},
    107: {"name":"Shampoo","category":"Personal Care","price":180,"stock":15},
    108: {"name":"Toothpaste","category":"Personal Care","price":95,"stock":20}}

# ------------------------------------------
# SHOPPING CART
# ------------------------------------------

cart = {}

# ------------------------------------------
# SALES INFORMATION
# ------------------------------------------

total_bills = 0
total_items = 0
total_sales = 0

# ------------------------------------------
# DISPLAY PRODUCTS
# ------------------------------------------

def display_products():
    print("\n")
    print("=" * 75)
    print("                         PRODUCT LIST")
    print("=" * 75)
    print("ID\tProduct Name\t\tCategory\t\tPrice\tStock")
    print("-" * 75)

    for product_id, product in products.items():
        print(product_id,"\t",
              product["name"],"\t\t",
              product["category"],"\t₹",
              product["price"],"\t",
              product["stock"])
    print("=" * 75)

# ------------------------------------------
# SEARCH PRODUCT
# ------------------------------------------

def search_product():
    search = input("\nEnter product name to search: ")
    found = False
    for product_id, product in products.items():
        if search.lower() in product["name"].lower():
            print("\nProduct Found")
            print("----------------------")
            print("Product ID :", product_id)
            print("Name       :", product["name"])
            print("Category   :", product["category"])
            print("Price      : ₹", product["price"])
            print("Stock      :", product["stock"])
            found = True
        if found == False:
            print("\nProduct not found.")

# ------------------------------------------
# ADD PRODUCT TO CART
# ------------------------------------------

def add_to_cart():
    try:
        product_id = int(input("\nEnter Product ID: "))
        if product_id not in products:
            print("Invalid Product ID.")
            return

        quantity = int(input("Enter quantity: "))
        if quantity <= 0:
            print("Quantity must be greater than 0.")
            return

        if quantity > products[product_id]["stock"]:
            print("Not enough stock available.")
            return

        if product_id in cart:
            new_quantity = cart[product_id] + quantity
            if new_quantity > products[product_id]["stock"]:
                print("Quantity exceeds available stock.")
                return

            cart[product_id] = new_quantity
        else:
            cart[product_id] = quantity
        print("\nProduct added to cart successfully.")
    except ValueError:
        print("\nPlease enter a valid number.")

# ------------------------------------------
# VIEW CART
# ------------------------------------------

def view_cart():
    if len(cart) == 0:
        print("\nCart is empty.")
        return

    print("\n")
    print("=" * 50)
    print("                    YOUR CART")
    print("=" * 50)

    total = 0
    for product_id, quantity in cart.items():
        product = products[product_id]
        amount = product["price"] * quantity
        print(product["name"], "x", quantity, "= ₹", amount)

        total = total + amount

    print("-" * 50)
    print("Cart Total : ₹", total)
    print("=" * 50)

# ------------------------------------------
# REMOVE PRODUCT FROM CART
# ------------------------------------------

def remove_from_cart():
    if len(cart) == 0:
        print("\nCart is empty.")
        return
    try:
        product_id = int(input("\nEnter Product ID to remove: "))
        if product_id not in cart:
            print("Product is not in the cart.")
            return

        del cart[product_id]
        print("Product removed from cart.")

    except ValueError:
        print("Please enter a valid Product ID.")

# ------------------------------------------
# GENERATE BILL
# ------------------------------------------

def generate_bill():
    global total_bills
    global total_items
    global total_sales

    if len(cart) == 0:
        print("\nCart is empty.")
        return

    print("\n")
    print("=" * 60)
    print("                    SHOPPING BILL")
    print("=" * 60)

    print("Date:",datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
    print("-" * 60)

    subtotal = 0
    items = 0

    for product_id, quantity in cart.items():
        product = products[product_id]
        amount = product["price"] * quantity
        print(product["name"],"x",quantity," = ₹",amount)

        subtotal = subtotal + amount
        items = items + quantity

    # --------------------------------------
    # DISCOUNT
    # --------------------------------------

    discount = 0
    if subtotal >= 1000:
        discount = subtotal * 0.10

    # --------------------------------------
    # TAX
    # --------------------------------------

    amount_after_discount = subtotal - discount
    tax = amount_after_discount * 0.05

    # --------------------------------------
    # FINAL AMOUNT
    # --------------------------------------

    grand_total = amount_after_discount + tax

    print("-" * 60)
    print("Total Items          :", items)
    print("Subtotal             : ₹", round(subtotal, 2))
    print("Discount             : ₹", round(discount, 2))
    print("Tax (5%)             : ₹", round(tax, 2))
    print("Grand Total          : ₹", round(grand_total, 2))
    print("=" * 60)
    print("              THANK YOU FOR SHOPPING!")
    print("=" * 60)

    # --------------------------------------
    # UPDATE STOCK
    # --------------------------------------

    for product_id, quantity in cart.items():
        products[product_id]["stock"] = (products[product_id]["stock"] - quantity)

    # --------------------------------------
    # UPDATE SALES INFORMATION
    # --------------------------------------

    total_bills = total_bills + 1
    total_items = total_items + items
    total_sales = total_sales + grand_total

    cart.clear()


# ------------------------------------------
# SALES REPORT
# ------------------------------------------

def sales_report():
    print("\n")
    print("=" * 45)
    print("                 SALES REPORT")
    print("=" * 45)
    print("Total Bills Generated :", total_bills)
    print("Total Items Sold      :", total_items)
    print("Total Sales           : ₹", round(total_sales, 2))

    if total_bills > 0:
        average_bill = total_sales / total_bills
        print("Average Bill          : ₹",round(average_bill, 2))
    else:
        print("Average Bill          : ₹ 0")
    print("=" * 45)

# ------------------------------------------
# MAIN MENU
# ------------------------------------------

while True:
    print("\n")
    print("=" * 45)
    print("       SHOPPING & BILLING SYSTEM")
    print("=" * 45)
    print("1. Display Products")
    print("2. Search Product")
    print("3. Add Product to Cart")
    print("4. View Cart")
    print("5. Remove Product from Cart")
    print("6. Generate Bill")
    print("7. Sales Report")
    print("8. Exit")
    print("=" * 45)

    try:
        choice = int(input("Enter your choice: "))

    except ValueError:
        print("\nPlease enter a number from 1 to 8.")
        continue

    # --------------------------------------
    # OPTION 1
    # --------------------------------------

    if choice == 1:
        display_products()

    # --------------------------------------
    # OPTION 2
    # --------------------------------------

    elif choice == 2:
        search_product()

    # --------------------------------------
    # OPTION 3
    # --------------------------------------

    elif choice == 3:
        add_to_cart()

    # --------------------------------------
    # OPTION 4
    # --------------------------------------

    elif choice == 4:
        view_cart()

    # --------------------------------------
    # OPTION 5
    # --------------------------------------

    elif choice == 5:
        remove_from_cart()

    # --------------------------------------
    # OPTION 6
    # --------------------------------------

    elif choice == 6:
        generate_bill()

    # --------------------------------------
    # OPTION 7
    # --------------------------------------

    elif choice == 7:
        sales_report()

    # --------------------------------------
    # OPTION 8
    # --------------------------------------

    elif choice == 8:
        print("\nThank you for using the Shopping & Billing System.")
        print("Goodbye!")

        break

    # --------------------------------------
    # INVALID OPTION
    # --------------------------------------

    else:
        print("\nInvalid choice.")
        print("Please select a number from 1 to 8.")