from typing import Any

from django.shortcuts import render
from drf_spectacular.types import OpenApiTypes
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Forecasting
from .serializers import ForecastingSerializers
from functional_part.geneator import create_graf
from drf_spectacular.utils import extend_schema, OpenApiParameter


# Create your views here.


class ForecastingView(APIView):
    @extend_schema(parameters=[
        OpenApiParameter(
            name='a',
            description='URL of the HTML page',
            type=OpenApiTypes.DATE,
            location=OpenApiParameter.QUERY,
            required=True
        ),
        OpenApiParameter(
            name='b',
            description='URL of the HTML page',
            type=OpenApiTypes.DATE,
            location=OpenApiParameter.QUERY,
            required=True
        ),
        OpenApiParameter(
            name='c',
            description='URL of the HTML page',
            type=OpenApiTypes.STR,
            location=OpenApiParameter.QUERY,
            required=True
        ),
    ],
        request=None,
        responses=ForecastingSerializers,
        methods=['GET'])
    def get(self, request):
        a = request.GET.get('a')
        b = request.GET.get('b')
        c = request.GET.get('c')
        create_graf(a, b, c)
        graphic = Forecasting(a, b, c, f'architecture_project/media/forecast.png')
        serial = ForecastingSerializers(instance=graphic)
        return Response(serial.data)
