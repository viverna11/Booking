from django.urls import path
from .views import room_list
from .views import room_detail
urlpatterns = [
    path("" ,room_list, name='room_list'),
    path("<int:pk>/" ,room_detail, name='room_details')
]