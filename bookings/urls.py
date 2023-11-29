from django.urls import path
from .views import reserve_table, menu_view, register_view

urlpatterns = [
    path('reserve/', reserve_table, name='reserve'),
    path('menu/', menu_view, name='menu'),
    path('register/', register_view, name='register')
    # add more paths as needed
]


# Django MVC
# Django Forms
# Django database (ORM) - camada que interage com db sem vc precisar escrever SQL na mao..
# Django unit test

# CRUD - Create, read update delete