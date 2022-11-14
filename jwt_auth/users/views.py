from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers
from rest_framework.views import APIView
# Create your views here.


class UserAPIView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self,request):
        content = {'message':'Hello,World'}
        return Response(content)