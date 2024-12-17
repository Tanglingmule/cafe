Café Management System
====================

A Django-based web application for managing a café's menu items, customers, and orders.

Features
--------
1. Menu Management
   - View all menu items
   - Add new menu items
   - Edit existing menu items
   - Items categorized as main dishes, snacks, and drinks

2. Customer Management
   - Store customer information (name and email)
   - Add new customers while creating orders
   - View existing customers

3. Order Management
   - Create new orders
   - Select multiple items per order
   - Calculate order totals
   - View order history

Setup
-----
1. Ensure Python and Django are installed
2. Run database migrations:
   python manage.py migrate

3. Add sample menu items:
   python add_menu_items.py

4. Add sample orders (optional):
   python add_sample_orders.py

5. Run the development server:
   python manage.py runserver

Usage
-----
1. Menu Items
   - View menu: Click "Menu" in navigation
   - Add item: Click "Add Menu Item" in navigation
   - Edit item: Use edit button on menu page

2. Orders
   - View orders: Home page shows all orders
   - Create order: Click "Create Order" in navigation
     * Choose existing customer or create new one
     * Select items from different categories
     * Submit order

3. Customers
   - Add while creating order
   - Required information: First name, Last name, Email

File Structure
-------------
/cafe/
  models.py  - Database models (MenuItem, Customer, Order)
  views.py   - View logic for displaying pages
  forms.py   - Forms for data input
  urls.py    - URL routing
  /templates/cafe/ - HTML templates
  /static/cafe/   - CSS and static files

Dependencies
-----------
- Django
- Python 3.x

Notes
-----
- Menu items are categorized as: main, snack, drink
- Orders show total price automatically
- Customer emails must be unique
- All prices are in GBP (£)
