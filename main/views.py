from rest_framework import viewsets
from .models import UserProfile, Category, Product
from .serializers import UserProfileSerializer, CategorySerializer, ProductSerializer
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.contrib.auth.models import User
from django.shortcuts import render

def test_page(request):
    return render(request, 'main/test_page.html')


def create_user(request):
    user = User.objects.create(username="new_user")
    
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "notifications",
        {
            "type": "send_notification",
            "message": f"Новый пользователь {user.username} был создан."
        }
    )
    return JsonResponse({"message": "User created"})



class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer