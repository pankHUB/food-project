from . import views
from django.urls import path
"""name spacing"""
app_name='food'
urlpatterns = [
    path('',views.index,name='index'),
    path('item/',views.item,name='item'),
    path('price/',views.price,name='price'),
    path('list/',views.lists,name='lists'),
    path('<int:item_id>/',views.detail,name='detail'),
]