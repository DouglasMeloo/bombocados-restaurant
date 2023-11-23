from django.urls import path
from .views import reserve_table, menu_view

urlpatterns = [
    path('reserve/', reserve_table, name='reserve'),
    path('menu/', menu_view, name='menu'),
    # add more paths as needed
]