from django.shortcuts import render


def home(request):
    return render(request, 'store/home.html')

def cart(request):
    return render(request, 'store/cart.html')

def contacts(request):
        return render(request, 'store/contacts.html')

def about(request):
    return render(request, 'store/about.html')

def menu(request):

    return render(request, 'store/menu.html')
