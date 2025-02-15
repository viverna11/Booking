from django.urls import path
from .views import room_list, room_detail, book_room


urlpatterns = [
    path("" ,room_list, name='room_list'),
    path("<int:pk>/" ,room_detail, name='room_details'),
    path("book-room", book_room, name='book_room')

]
