from django.db import models

# Create your models here.


class Forecasting:
    def __init__(self, a, b, c, d):
        self.first_date = a
        self.last_date = b
        self.color = c
        self.file_way = d
