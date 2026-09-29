from datetime import datetime
total_bills=0
total_items=0
total_sales=0

def generate_bill(products,cart):
    global total_bills,total_items,total_sales
    if not cart:
        print("Cart is empty.")
        return
    subtotal=0
    items=0
    print("\n========== BILL ==========")
    print("Date:",datetime.now().strftime("%d-%m-%Y %H:%M"))
    for pid,qty in cart.items():
        p=products[pid]
        amount=p["price"]*qty
        subtotal+=amount
        items+=qty
        print(p["name"],"x",qty,"= ₹",amount)
    discount=0
    if subtotal>=1000:
        discount=subtotal*0.10
    amount_after_discount=subtotal-discount
    tax=amount_after_discount*0.05
    grand_total=amount_after_discount+tax
    print("--------------------------")
    print("Subtotal: ₹",round(subtotal,2))
    print("Discount: ₹",round(discount,2))
    print("Tax: ₹",round(tax,2))
    print("Grand Total: ₹",round(grand_total,2))
    print("==========================")
    for pid,qty in cart.items():
        products[pid]["stock"]-=qty
    total_bills+=1
    total_items+=items
    total_sales+=grand_total
    cart.clear()

def sales_report():
    print("\n========== SALES REPORT ==========")
    print("Total Bills:",total_bills)
    print("Total Items Sold:",total_items)
    print("Total Sales: ₹",round(total_sales,2))
    if total_bills>0:
        print("Average Bill: ₹",round(total_sales/total_bills,2))
    else:
        print("Average Bill: ₹ 0")