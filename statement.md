# Vityarthi - Shopping & Billing System

## Project Statement

The **Vityarthi - Shopping & Billing System** is a console-based Python project developed for **CSE1021**. The main purpose of this project is to create a simple shopping and billing system while learning and applying basic Python programming concepts.

The system allows a user to view and search products, add products to a shopping cart, remove products, view the cart, generate a bill, and generate a sales report.

## Objectives

* To create a simple shopping system using Python.
* To understand and use functions in Python.
* To practice lists and dictionaries.
* To use loops and conditional statements.
* To perform calculations using arithmetic operators.
* To implement input validation.
* To manage product stock.
* To generate bills and sales reports.
* To understand how multiple Python files can work together in a project.

## Main Features

1. **Display Products**

   * Shows the available products and their prices.
   * Products include grocery, dairy, snacks, and personal-care items.

2. **Search Products**

   * Allows the user to search for a product.

3. **Add to Cart**

   * Users can add available products to their shopping cart.
   * The system checks product availability and quantity.

4. **View Cart**

   * Displays the products currently added to the cart.
   * Shows quantities and prices.

5. **Remove from Cart**

   * Allows users to remove products from their cart.

6. **Generate Bill**

   * Calculates the total amount of the purchase.
   * Applies a **10% discount when the subtotal is ₹1000 or more**.
   * Applies **5% tax after the discount**.
   * Displays the final bill.

7. **Stock Management**

   * Product stock is reduced after a successful purchase.

8. **Sales Report**

   * Generates a report containing information about completed sales.

## Technologies Used

* **Programming Language:** Python
* **Interface:** Console / Terminal
* **External Libraries:** None

## Python Concepts Used

The project uses the following basic Python concepts:

* Variables
* Data types
* Lists
* Dictionaries
* Functions
* Loops
* Conditional statements
* Arithmetic operations
* Input and output
* Input validation
* Modules and imports
* Date and time handling

## Project Structure

```text
Vityarthi/
│
├── main.py
├── products.py
├── cart.py
├── billing.py
├── reports.py
├── validation.py
└── statement.md
```

## File Description

### `main.py`

Contains the main menu and controls the overall flow of the program.

### `products.py`

Contains product information and functions for displaying and searching products.

### `cart.py`

Handles adding, viewing, and removing products from the shopping cart.

### `billing.py`

Calculates the subtotal, discount, tax, and final bill.

### `reports.py`

Generates the sales report.

### `validation.py`

Contains functions used to validate user input and prevent invalid entries.

## Billing Rules

The billing system follows these rules:

* If subtotal is **₹1000 or more**, a **10% discount** is applied.
* A **5% tax** is applied after the discount.
* The final amount is calculated after applying the discount and tax.
* Purchased quantities are deducted from available stock.

## Limitations

* The project is console-based and does not have a graphical user interface.
* No database is used.
* The project does not use classes or object-oriented programming.
* Sales information is handled using basic Python data structures.

## Conclusion

The Vityarthi project demonstrates how basic Python programming concepts can be combined to create a functional shopping and billing system. It provides practical experience with functions, lists, dictionaries, loops, conditions, validation, calculations, and multiple Python modules.

**Project Name:** Vityarthi - Shopping & Billing System
**Author:** Garvith Nalwaya
