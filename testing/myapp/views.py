from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from myapp.models import TODOList
from myapp.serializers import TODOserializers
from myapp.permissions import IsOwner

# Create your views here.

class TODOListView(ListCreateAPIView):
    queryset = TODOList.objects.all()
    serializer_class = TODOserializers
    permission_classes = (IsAuthenticated,)

class TODODetailView(RetrieveUpdateDestroyAPIView):
    queryset = TODOList.objects.all()
    serializer_class = TODOserializers
    permission_classes = (IsOwner,)