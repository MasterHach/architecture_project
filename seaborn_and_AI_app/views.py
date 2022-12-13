import mimetypes
import os
from PIL import Image
import PIL
from django.core.files import File

from django.shortcuts import render
from django.http import HttpResponse, FileResponse, HttpResponseBadRequest
# Create your views here.
import functional_part
from seaborn_and_AI_app.models import Grafic


def index(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    c = request.GET.get('c')
    fig_name = functional_part.create_graf(a, b, c)
    if fig_name != 'forecast.png':
        return HttpResponseBadRequest(f'Mdaa... {fig_name}')
    context = {
        'name': fig_name
    }
    return render(request, './seaborn_and_AI_app/result.html', context)
