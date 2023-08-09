from django.urls import path
from . import views
app_name='eshopapp'
urlpatterns = [
    #path('',views.index,name='index' ),
    path('admino/',views.admino,name='admino' ),
    path('category/',views.category,name='category' ),
    path('seller/',views.seller,name='seller' ),
    path('product/',views.product,name='product' ),
    path('addcart/<int:pid>',views.addcart,name='addcart' ),
    #path('buyprod/',views.buyprod,name='buyprod' ),
    path('',views.register,name='register' ),
    path('login/',views.login,name='login' ),
    #path('findprod/<str:canm>/',views.findprod,name='findprod' ),
    
   # path('register/',views.register,name='register' ),
    path('dellogininfo/',views.dellogininfo,name='dellogininfo'),
   # path('adminsession/',views.adminsession,name='adminsession'),
   path('cartdisplay/',views.cartdisplay,name='cartdisplay'),
   path('checkout/<int:pid>/',views.checkoutedit,name='checkout'),

]
