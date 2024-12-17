import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'runshaw_cafe.settings')
django.setup()

from cafe.models import MenuItem

menu_items = [
    # Main dishes
    {'name': 'Pot noodle', 'category': 'main', 'price': 1.50},
    {'name': 'Tuna sandwich', 'category': 'main', 'price': 2.50},
    {'name': 'Ham wrap', 'category': 'main', 'price': 3.00},
    {'name': 'Falafel wrap', 'category': 'main', 'price': 2.00},
    {'name': 'Chicken wrap', 'category': 'main', 'price': 3.50},
    
    # Snacks
    {'name': 'Cookie', 'category': 'snack', 'price': 1.25},
    {'name': 'Curry crisps', 'category': 'snack', 'price': 0.50},
    {'name': 'Frutella', 'category': 'snack', 'price': 0.80},
    {'name': 'Flapjack', 'category': 'snack', 'price': 1.70},
    
    # Drinks
    {'name': 'Diet coke', 'category': 'drink', 'price': 1.50},
    {'name': 'Diet Fanta', 'category': 'drink', 'price': 1.50},
    {'name': 'Rio', 'category': 'drink', 'price': 1.40},
    {'name': 'Pure orange juice', 'category': 'drink', 'price': 2.00},
    {'name': 'Milkshake', 'category': 'drink', 'price': 2.50},
    {'name': 'Coffee', 'category': 'drink', 'price': 0.50},
]

# Clear existing menu items
MenuItem.objects.all().delete()

# Add new menu items
for item in menu_items:
    MenuItem.objects.create(**item)

print("Menu items added successfully!")
