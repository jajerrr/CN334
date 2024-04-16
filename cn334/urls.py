from django.contrib import admin
from django.urls import path
from ecommerce import views as ecom_views

urlpatterns =[

    path('admin/', admin.site.urls),
    path("ecommerce/", ecom_views.ecommerce_index_view),
    path("ecommerce/item/<item_id>", ecom_views.item_view),
    path("ecommerce/Homepage", ecom_views.Homepage),
    path("ecommerce/Contactpage", ecom_views.Contactpage),
    path("ecommerce/Categorypage", ecom_views.Categorypage),
    path("ecommerce/Checkoutpage", ecom_views.Checkoutpage),
    path("ecommerce/Productpage", ecom_views.Productpage),
    path("w09/request", ecom_views.basic_request),
    path("w09/tokenize", ecom_views.tokenize),
    path("w09/sentimental", ecom_views.sentimental),
    path("w09/text2speech", ecom_views.text2speech)
    
]
