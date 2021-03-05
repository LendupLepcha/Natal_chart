from django.urls import path
from . import views
app_name = 'chart'

urlpatterns = [
    path('create/', views.view_create, name = 'create'),
    path('show/', views.view_show, name = 'show'),
    path('search/', views.view_search, name = 'search'),
    path('search_results/', views.view_search_results, name = 'search_results'),
]
