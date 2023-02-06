
from django.contrib import admin
from django.urls import path, include
from home import views
from home.views import herb_list, herb_view,home

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.HomeView.as_view(), name='home'),
    path('herb/', herb_list),
    path('herb/<pk>', herb_view),
    path('', home)
]
