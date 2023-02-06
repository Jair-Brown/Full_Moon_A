from django.urls import path
from . import views
from home.views import herb_list, herb_view,home

app_name = 'home'
urlpatterns = [
    path( 'herb/list', herb_list, name = 'herb'),
    path( 'herb/<id>', herb_view),
    path('', home, name='home'),
]