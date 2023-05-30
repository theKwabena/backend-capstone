from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet

from rest_framework.permissions import IsAuthenticated
from .models import Booking
from LittleLemonAPI.serializers import MenuItemSerializer, BookingSerializer

# Create your views here.
def index(request):
    return render(request, 'index.html', {})




class BookingViewSet(ModelViewSet):
    permission_classes = IsAuthenticated
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer