from django.urls import path

from . import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('shop',views.shop,name = "shop"),
    path('cart',views.cart,name = "cart"),
    path('sell',views.sell,name = 'sell'),
    path('login',views.login,name = 'login'),
    path('signup',views.signup,name="signup")
]