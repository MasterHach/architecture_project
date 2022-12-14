from typing import Any

from django.shortcuts import render
from drf_spectacular.types import OpenApiTypes
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Forecasting
from .serializers import ForecastingSerializers
from functional_part.geneator import create_graf
from functional_part.geneator import encode_image
from drf_spectacular.utils import extend_schema, OpenApiParameter
import base64

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
        name = create_graf(a, b, c)
        if name != 'forecast.png':
            return Response(f'Error 400. Bad Request: {name}', status=400)
        # with open('./media/forecast.png', 'rb') as img:
        #     image_read = img.read()
        #     res_img = str(base64.b64encode(image_read))
        enc_name = encode_image('./media/forecast.png')
        graphic = Forecasting(a, b, c, f'architecture_project/media/forecast.png', enc_name, 'utf-8')
        serial = ForecastingSerializers(instance=graphic)
        return Response(serial.data)
