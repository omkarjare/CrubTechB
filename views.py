from django.shortcuts import render, redirect
from .forms import Order, OrderForm



def order_view(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    template_name = 'app1/order.html'
    context = {'form': form}
    return render(request, template_name, context)


def show_view(request):
    data = Order.objects.all()
    template_name = 'app1/show.html'
    context = {'data': data}
    return render(request, template_name, context)

def update_view(request, pk):
    obj = Order.objects.get(id=pk)
    form = OrderForm(instance=obj)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    template_name = 'app1/order.html'
    context = {'form': form}
    return render(request, template_name, context)


def delete_view(request, pk):
    if request.method == 'POST':
        obj = Order.objects.get(id=pk)
        obj.delete()
        return redirect('show_url')
    template_name = 'app1/confirm.html'
    context = {}
    return render(request, template_name, context)