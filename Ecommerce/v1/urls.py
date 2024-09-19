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
    path('signup',views.signup,name="signup"),
    path('addCart/<str:id>',views.addCart,name="addCart"),
    path('deleteCart/<str:id>',views.deleteCart,name="deleteCart"),
    path('cartNumber',views.cartNumber,name = "cartNumber"),
    path('searchShop',views.searchShop,name = "searchShop"),
    path('confirmPurchase',views.confirmPurchase,name = "confirmPurchase"),

]