import os
import django
from decimal import Decimal

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'runshaw_cafe.settings')
django.setup()

from cafe.models import MenuItem, Customer, Order

# Clear existing data
Order.objects.all().delete()
Customer.objects.all().delete()

# Create customers
customers = [
    {
        'forename': 'John',
        'surname': 'Smith',
        'email': 'john.smith@email.com',
        'balance': Decimal('20.00')
    },
    {
        'forename': 'Emma',
        'surname': 'Wilson',
        'email': 'emma.wilson@email.com',
        'balance': Decimal('15.00')
    },
    {
        'forename': 'Michael',
        'surname': 'Brown',
        'email': 'michael.brown@email.com',
        'balance': Decimal('25.00')
    },
    {
        'forename': 'Sarah',
        'surname': 'Davis',
        'email': 'sarah.davis@email.com',
        'balance': Decimal('30.00')
    },
    {
        'forename': 'David',
        'surname': 'Taylor',
        'email': 'david.taylor@email.com',
        'balance': Decimal('18.00')
    }
]

# Create customers
created_customers = []
for customer_data in customers:
    customer = Customer.objects.create(**customer_data)
    created_customers.append(customer)

# Get all menu items
main_dishes = list(MenuItem.objects.filter(category='main'))
snacks = list(MenuItem.objects.filter(category='snack'))
drinks = list(MenuItem.objects.filter(category='drink'))

# Create sample orders
orders_data = [
    # John's orders
    {
        'customer': created_customers[0],
        'items': [
            main_dishes[0],  # Pot noodle
            snacks[0],      # Cookie
            drinks[0]       # Diet coke
        ]
    },
    # Emma's orders
    {
        'customer': created_customers[1],
        'items': [
            main_dishes[1],  # Tuna sandwich
            snacks[1],      # Curry crisps
            drinks[1]       # Diet Fanta
        ]
    },
    # Michael's orders
    {
        'customer': created_customers[2],
        'items': [
            main_dishes[2],  # Ham wrap
            snacks[2],      # Frutella
            drinks[2]       # Rio
        ]
    },
    # Sarah's orders
    {
        'customer': created_customers[3],
        'items': [
            main_dishes[3],  # Falafel wrap
            snacks[3],      # Flapjack
            drinks[3]       # Pure orange juice
        ]
    },
    # David's orders
    {
        'customer': created_customers[4],
        'items': [
            main_dishes[4],  # Chicken wrap
            drinks[4]       # Milkshake
        ]
    }
]

# Create orders
for order_data in orders_data:
    order = Order.objects.create(customer=order_data['customer'])
    order.items.set(order_data['items'])
    print(f"Created order for {order.customer} with {len(order_data['items'])} items")

print("\nSample orders created successfully!")
