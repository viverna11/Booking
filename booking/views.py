from django.shortcuts import render
from .models import Room
def room_list(request):
    rooms = Room.objects.all()
    context = {
        'rooms': rooms
    }
    return render(request, 'booking/room_list.html', context)
def room_detail(request, pk):
    room = Room.objects.get(id=pk)
    context = {
        'room': room
    }
    return render(request, 'booking/room_details.html', context)