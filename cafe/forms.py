# Import necessary Django modules
from django import forms
from .models import Order, Customer, MenuItem

class CustomerForm(forms.ModelForm):
    """Form for creating a new customer.
    
    Fields:
    - forename: Customer's first name
    - surname: Customer's last name
    - email: Customer's email address (must be unique)
    """
    class Meta:
        model = Customer
        fields = ['forename', 'surname', 'email']
        widgets = {
            'forename': forms.TextInput(attrs={'class': 'form-control'}),
            'surname': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'})
        }

class OrderForm(forms.Form):
    """Form for creating a new order.
    
    Fields:
    - customer_type: Radio buttons to choose between existing or new customer
    - existing_customer: Dropdown to select an existing customer
    - items: Multiple choice field for selecting menu items
    """
    CUSTOMER_CHOICE = (
        ('existing', 'Select Existing Customer'),
        ('new', 'Create New Customer')
    )
    
    customer_type = forms.ChoiceField(
        choices=CUSTOMER_CHOICE,
        widget=forms.RadioSelect,
        initial='existing'
    )
    
    existing_customer = forms.ModelChoiceField(
        queryset=Customer.objects.all(),
        empty_label="Select a customer",
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=False
    )
    
    items = forms.ModelMultipleChoiceField(
        queryset=MenuItem.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )
