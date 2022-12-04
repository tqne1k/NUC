from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class Test(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    def get_object(self):
        return self.request.HttpResponse("Hello world!")