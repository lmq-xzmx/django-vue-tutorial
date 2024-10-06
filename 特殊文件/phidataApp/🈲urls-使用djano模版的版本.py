from django.urls import path
from . import views
app_name = 'phidataApp'
urlpatterns = [
    path('get_user_input/', views.get_user_input, name='get_user_input'),
]
