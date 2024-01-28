from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def ecommerce_index_view(request):
    '''This function render index page of ecommerce views'''

    return HttpResponse('Welcome to 6310742140 Achiraya Komatsu views!')

def item_view(request, item_id):   
    context_data = {
        "item_id": item_id   
    }
    return render(request, 'index.html',context= context_data)
def Homepage(request):
    return render(request, 'Homepage.html')

def Categorypage(request):
    return render(request, 'Categorypage.html')

def Productpage(request):
    return render(request, 'Productpage.html')

def Checkoutpage(request):
    return render(request, 'Checkoutpage.html')

def Contactpage(request):
    return render(request, 'Contactpage.html')
