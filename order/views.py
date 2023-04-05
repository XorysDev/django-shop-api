from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from order.models import Order


class OrderApiView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class =
