from django.urls import path , include
from . import views
from rest_framework import routers


rr = routers.DefaultRouter()
rr.register('', views.orderitem)

rrr = routers.DefaultRouter()
rrr.register('', views.order)


r = routers.DefaultRouter()
r.register('', views.product)

urlpatterns = [
    path('Category/',views.Category_listAPI,name='category'), 
    path('order/', include(rrr.urls)),
    path('itemorder/', include(rr.urls)),
    path('Recommended/',views.Recommended_listAPI,name='Recommended'),
    path('', include(r.urls)),
    
    
    

]