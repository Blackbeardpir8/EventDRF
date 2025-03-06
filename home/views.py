from django.shortcuts import render
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import Event, EventSerializer, RegisterSerializer, LoginSerializer
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
# Create your views here.

class RegisterAPI(APIView):
    def post(self,request):
        data = request.data
        serializer = RegisterSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status" : True,
                "message" : "Account Created",
                "data" : serializer.data
            })
        
        return Response({
            "status" : False,
            "message" : "Account not Created",
            "error" : serializer.errors
        })
        return Response('hello')
    
class LoginAPI(APIView):
    def post(self, request):
        data = request.data
        serializer = LoginSerializer(data = data)
        if serializer.is_valid():
            user = authenticate(
                username = serializer.validated_data['username'],
                password = serializer.validated_data['password']
            )
            if user:
                token, created = Token.objects.get_or_create(user = user)
                return Response({
                    "status" : True,
                    "message" : "Login Successfull",
                    "data" : {"token" : token.key}
                })
            else:
                return Response({
                    "status" : False,
                    "message" : "Invalid Credentials",
                    "data" : {}
                })
        return Response({
            "status" : False,
            "message" : "Login Failed",
            "error" : serializer.errors
        })
    
class PublicEventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    
class PrivateEventViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Event.objects.all()
    serializer_class = EventSerializer

