import mimetypes
import os

from django.shortcuts import render
from django.http import HttpResponse, FileResponse
# Create your views here.
import functional_part


def index(request, a, b, c):
    functional_part.create_graf(a, b, c)

    # response = FileResponse(open('forecast.png', 'rb'))
    # return HttpResponse(response)
    return render(request, './seaborn_and_AI_app/result.html')
    #return HttpResponse('<a href="./forecast.png" download><img src="./forecast.png" alt="download graf"/></a>',
                        #content_type="text/html", charset="utf-8")
