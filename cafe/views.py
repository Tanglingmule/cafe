# Import necessary Django modules
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import MenuItem, Customer, Order
from django import forms
from .forms import OrderForm, CustomerForm

class MenuItemForm(forms.ModelForm):
    """Form for creating and editing menu items."""
    class Meta:
        model = MenuItem
        fields = ['name', 'category', 'price']

class HomeView(ListView):
    """Display all orders on the home page.
    
    Lists orders in reverse chronological order and calculates
    the total price for each order.
    """
    model = Order
    template_name = 'cafe/home.html'
    context_object_name = 'orders'
    ordering = ['-order_date']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Calculate total price for each order
        for order in context['orders']:
            order.total = sum(item.price for item in order.items.all())
        return context

class MenuListView(ListView):
    """Display all menu items."""
    model = MenuItem
    template_name = 'cafe/menu_list.html'
    context_object_name = 'menu_items'

class MenuItemCreateView(CreateView):
    """Handle creation of new menu items."""
    model = MenuItem
    form_class = MenuItemForm
    template_name = 'cafe/menuitem_form.html'
    success_url = reverse_lazy('success')

    def form_valid(self, form):
        messages.success(self.request, 'Menu item added successfully!')
        return super().form_valid(form)

class MenuItemUpdateView(UpdateView):
    """Handle updating existing menu items."""
    model = MenuItem
    form_class = MenuItemForm
    template_name = 'cafe/menuitem_form.html'
    success_url = reverse_lazy('success')

    def form_valid(self, form):
        messages.success(self.request, 'Menu item updated successfully!')
        return super().form_valid(form)

def success_view(request):
    """Simple view to show success message after operations."""
    return render(request, 'cafe/success.html')

def create_order(request):
    """Handle creation of new orders.
    
    This view handles both creation of new customers and
    selection of existing customers when creating an order.
    """
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        customer_form = CustomerForm(request.POST)
        
        if order_form.is_valid():
            customer_type = order_form.cleaned_data['customer_type']
            items = order_form.cleaned_data['items']
            
            # Handle customer selection/creation
            if customer_type == 'existing':
                customer = order_form.cleaned_data['existing_customer']
                if not customer:
                    messages.error(request, 'Please select an existing customer')
                    return render(request, 'cafe/create_order.html', {
                        'order_form': order_form,
                        'customer_form': customer_form
                    })
            else:  # new customer
                if customer_form.is_valid():
                    customer = customer_form.save()
                else:
                    return render(request, 'cafe/create_order.html', {
                        'order_form': order_form,
                        'customer_form': customer_form
                    })
            
            # Create the order
            order = Order.objects.create(customer=customer)
            order.items.set(items)
            
            messages.success(request, 'Order created successfully!')
            return redirect('home')
    else:
        order_form = OrderForm()
        customer_form = CustomerForm()
    
    return render(request, 'cafe/create_order.html', {
        'order_form': order_form,
        'customer_form': customer_form
    })
