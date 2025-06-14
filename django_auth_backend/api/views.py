from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.db import IntegrityError
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
@permission_classes([AllowAny]) # Allow any user (authenticated or not) to access this view
def signup(request):
    """
    Handles user registration.
    """
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response(
            {"message": "Username and password are required"},
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        # create_user handles password hashing automatically
        user = User.objects.create_user(username=username, password=password)
        user.save()
        return Response(
            {"message": "User created successfully"},
            status=status.HTTP_201_CREATED
        )
    except IntegrityError:
        # This error occurs if the username already exists
        return Response(
            {"message": "Username already exists"},
            status=status.HTTP_409_CONFLICT
        )

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    """
    Handles user login.
    """
    username = request.data.get('username')
    password = request.data.get('password')

    # The 'authenticate' function checks credentials and returns a user object if valid
    user = authenticate(username=username, password=password)

    if user is not None:
        # Login successful
        return Response(
            {"message": "Login successful", "username": user.username},
            status=status.HTTP_200_OK
        )
    else:
        # Invalid credentials
        return Response(
            {"message": "Invalid username or password"},
            status=status.HTTP_401_UNAUTHORIZED
        )