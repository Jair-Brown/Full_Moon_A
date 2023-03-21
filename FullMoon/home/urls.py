from django.urls import path
from . import views


app_name = 'home'
urlpatterns = [
    path('', views.home, name = 'home'),
    path('list/', views.herb_list, name = 'list'),
    path('list/<str:name>/', views.herb_view, name ='herb_view'),
    
    
]