from . import views
from django.urls import path
"""name spacing"""
app_name='food'
urlpatterns = [
    path('',views.IndexClassView.as_view(),name='index'),
    path('item/',views.item,name='item'),
    path('price/',views.price,name='price'),
    path('list/',views.lists,name='lists'),
    path('<int:pk>/',views.FoodDetail.as_view(),name='detail'),
    #add items
    path('add/',views.CreateItem.as_view(),name='create_item'),
    # edit item
    path('update/<int:id>/',views.upadte_item,name='upade_item'),
    #delete item
    path('upadte/<int:id>/',views.delete_item,name='delete_item')
]