from django.urls import path

from .views import herb_list, herb_view, home, SearchResultsView



app_name = 'home'
urlpatterns = [
    path('', home, name='home'  ),
    # path('list/', HerbListView.as_view(), name='list'),
    path('list/', herb_list, name='list'),
    path('list/<str:name>/', herb_view, name='herb_view'),
    path('search/', SearchResultsView.as_view(), name="search_results"),

]