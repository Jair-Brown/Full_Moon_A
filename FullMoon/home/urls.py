from django.urls import path
from . import views


app_name = 'home'
urlpatterns = [
    path('list/', views.herb_list, name = 'list'),
    path('<int:id>/', views.herb_view, name ='herb_view'),
    # path('', home, name='home'),
    
]