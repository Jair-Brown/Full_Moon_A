
from django.contrib import admin
from django.urls import path, include
from home import views
from home.views import herb_list, herb_view,home

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('herb/<pk>', herb_view),
    # path('list/', herb_list),
    path('home/', home, name = 'home'),
    #figure out how to properly setup *include* links
    # path('herb/', include('home.urls')),
    path('list/', views.herb_list, name = 'list'),
    path('list/<int:id>/', views.herb_view, name ='herb_view'),
]
