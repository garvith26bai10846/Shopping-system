from product_cart import products,cart,display_products,search_product,add_to_cart,view_cart,remove_from_cart
from billing_report import generate_bill,sales_report

while True:
    print("\n===== SHOPPING AND BILLING SYSTEM =====")
    print("1. Display Products")
    print("2. Search Product")
    print("3. Add Product to Cart")
    print("4. View Cart")
    print("5. Remove Product from Cart")
    print("6. Generate Bill")
    print("7. Sales Report")
    print("8. Exit")
    choice=input("Enter your choice: ")
    if choice=="1":
        display_products()
    elif choice=="2":
        search_product()
    elif choice=="3":
        add_to_cart()
    elif choice=="4":
        view_cart()
    elif choice=="5":
        remove_from_cart()
    elif choice=="6":
        generate_bill(products,cart)
    elif choice=="7":
        sales_report()
    elif choice=="8":
        print("Thank you for using the system.")
        break
    else:
        print("Invalid choice.")