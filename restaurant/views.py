from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from rest_framework import viewsets, generics, status
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, MenuItemSerializer, BookingSerializer, BookingsSerializer
from .models import Menu, Booking
from .forms import BookingForm, LoginForm
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from datetime import datetime


@login_required
def home(request):   
    return render(request, 'index.html')

@login_required
def about(request):
    return render(request, 'about.html')

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    
class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer
    
    def get(self, request):
        menu = Menu.objects.all()
        return render(request, 'menu.html', {'menu': menu})


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer
    
    def post(self, request):
        permission_classes = [IsAuthenticated]
        
    def dispatch(self, request, *args, **kwargs):
        if request.method != "GET" and not request.user.is_authenticated:
            return redirect('/login/')
        return super().dispatch(request, *args, **kwargs)
    
    
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/login/')
    
        return super().dispatch(request, *args, **kwargs)
    
    
    def list(self, request):
        if not request.user.is_authenticated:
            return redirect('/login/')
        
        return render(request, 'book.html', {'form': BookingForm})
    

    def create(self, request):
        if not request.user.is_authenticated:
            return redirect('/login/')
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        name = serializer.validated_data.get("name")
        no_of_guests = serializer.validated_data.get("no_of_guests")
        reservation_date = serializer.validated_data.get("reservation_date")
        reservation_slot = serializer.validated_data.get("reservation_slot")
        
        exist = Booking.objects.filter(reservation_date=reservation_date, reservation_slot=reservation_slot)
        
        if exist.exists():
            return render(request, 'book.html', {'form': BookingForm, 'error': 'Slot already booked'}, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
       
        return render(request, 'book.html', {'form': BookingForm})

    
class BookingsView(generics.ListAPIView):
    serializer_class = BookingsSerializer
    
    def get(self, request):
        date = request.GET.get('date')
        if date:
            bookings = Booking.objects.all().filter(reservation_date=date)
        else:
            bookings = Booking.objects.all()
            
        booking_data = list(bookings.values())
        
        return JsonResponse(booking_data, safe=False)
    
    