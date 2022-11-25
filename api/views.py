from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Forecasting
from .serializers import ForecastingSerializers
from functional_part.geneator import create_graf
# Create your views here.


class ForecastingView(APIView):

    def get(self, request):
        a = request.GET.get('a')
        b = request.GET.get('b')
        c = request.GET.get('c')
        create_graf(a, b, c)
        graphic = Forecasting(a, b, c, f'architecture_project/media/forecast.png')
        serial = ForecastingSerializers(instance=graphic)
        return Response(serial.data)
