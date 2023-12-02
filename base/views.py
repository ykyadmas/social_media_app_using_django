from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Room
from .forms import RoomForms


def home(request):
 rooms=Room.objects.all()
 context={'rooms':rooms}
 return render(request,'base/home.html',context)
 
def room(request,pk):
    room=Room.objects.get(id=pk)
    context={'room':room}
    return render(request,'base/room.html',context) 
def create_room(request):
    form=RoomForms()
    if request.method=='POST':
       form=RoomForms(request.POST)
       if form.is_valid():
           form.save()
       return redirect('home')
    
    context={'form':form}
    return render(request,'base/create_room.html',context)
def update_room(request,pk):
    room=Room.objects.get(id=pk)
    form = RoomForms(instance=room)
    if(request.method=='POST'):
       form=RoomForms(request.POST,instance=room)
       if form.is_valid():
           form.save()
       return redirect('home')
    
   
    context={'form':form}
    return render(request,'base/create_room.html',context)
 
def delete_room(request,pk):
  room=Room.objects.get(id=pk)
  if request.method=='POST':
      room.delete()
      return redirect('home')
  return render(request,'base/delete.html',{'obj':room})
    