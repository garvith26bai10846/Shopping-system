# Shopping-system
The shopping system is a project that demonstrates how basic programming concepts can be used to solve a real world shopping problem. It provides product management, shopping cart operations,, billing, stock management and sales reporting through a console based interference.
# Shopping and Billing System

## Project Overview

The Shopping and Billing System is a simple console-based Python project.

It allows a user to view products, search for products, add products to a shopping cart, remove products, generate a bill, and view a sales report.

The project is created using basic Python concepts and does not use classes or GUI.

---

## Project Objectives

The main objectives of this project are:

- To create a simple shopping system using Python.
- To practice functions and dictionaries.
- To use loops and conditional statements.
- To perform billing and calculation of discounts and taxes.
- To manage product stock.
- To generate a simple sales report.
- To apply problem-solving concepts learned in CSE1021.

---

## Features

The project contains the following features:

### 1. Display Products

Displays all available products with:

- Product ID
- Product Name
- Category
- Price
- Stock

### 2. Search Product

The user can search for a product by entering its name.

### 3. Add Product to Cart

The user can:

- Enter a product ID.
- Enter the required quantity.
- Add the product to the shopping cart.

The program also checks whether enough stock is available.

### 4. View Cart

Displays:

- Product name
- Quantity
- Individual amount
- Total cart amount

### 5. Remove Product from Cart

The user can remove a product from the shopping cart using its product ID.

### 6. Generate Bill

The system generates a bill containing:

- Date and time
- Products purchased
- Quantity
- Subtotal
- Discount
- Tax
- Grand total

### 7. Discount

If the subtotal is ₹1000 or more, a 10% discount is applied.

### 8. Tax

A 5% tax is calculated after applying the discount.

### 9. Sales Report

The system displays:

- Total bills generated
- Total items sold
- Total sales
- Average bill amount

### 10. Stock Management

After generating a bill, the purchased quantity is automatically removed from the available stock.

---

## Technologies Used

- Python
- Python Dictionaries
- Python Functions
- Loops
- Conditional Statements
- Basic Arithmetic
- `datetime` module

---

## Requirements

To run this project, you need:

- Python 3.x
- Any Python editor such as:
  - VS Code
  - IDLE
  - PyCharm

No external Python libraries are required.

---

## How to Run

### Step 1

Download or copy the project.

### Step 2

Make sure the file is named:

```text
main.py
