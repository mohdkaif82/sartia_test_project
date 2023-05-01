
from moviepy.editor import VideoFileClip, TextClip, ImageClip, CompositeVideoClip
import os
from django.conf import settings
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect


from django.shortcuts import render

from rest_framework.response import  Response
from rest_framework.views import APIView
# from .utils import get_tokens_for_user

from django.views import View


from rest_framework import status
from .forms import ImageForm
from rest_framework.response import  Response
from rest_framework.views import APIView
# from .utils import get_tokens_for_user
from rest_framework.authentication import TokenAuthentication

# Create your views here.
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import  Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
# from .utils import get_tokens_for_user
from .serializers import RegistrationSerializer, PasswordChangeSerializer
# Create your views here.
import csv

# Create your views here.

import csv
from rest_framework.generics import ListCreateAPIView

from rest_framework.authtoken.models import Token
def index(request):
    return HttpResponse("hello ")

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    token=Token.objects.get_or_create(user=user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
        'token':str(token)
        
    }

class postapi(ListCreateAPIView):
    queryset = news.objects.all()
    serializer_class = User

class RegistrationView(APIView):
    permission_classes = ''
    authentication_classes = ''
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        ser=serializer
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": ser.data}) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    authentication_classes=''
    permission_classes=''
    def post(self, request):
        if 'email' not in request.data or 'password' not in request.data:
            return Response({'msg': 'Credentials missing'}, status=status.HTTP_400_BAD_REQUEST)
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            auth_data = get_tokens_for_user(user)
            return Response({'msg': 'Login Success', **auth_data}, status=status.HTTP_200_OK)
        return Response({'msg': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({'msg': 'Successfully Logged out'}, status=status.HTTP_200_OK)



class ChangePasswordView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def post(self, request):
        serializer = PasswordChangeSerializer(context={'request': request}, data=request.data)
        serializer.is_valid(raise_exception=True) #Another way to write is as in Line 17
        request.user.set_password(serializer.validated_data['new_password'])
        request.user.save()
        return Response({"msg":'Password has been changed'})

def logout_view(request):
    logout(request)
    return redirect('/auth/login/')




