from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from functional_part import geneator


class ForecastingTest(APITestCase):
    def test_forecast_1(self):
        url = reverse('forecast')
        response = self.client.get(url, data={'a': "2022-11-12", 'b': '2022-12-10', 'c': 'red'})
        self.assertEqual(response.data["byte_code"][0:40],
            "iVBORw0KGgoAAAANSUhEUgAABtMAAAVwCAYAAAA+")

    def test_forecast_2(self):
        url = reverse('forecast')
        response = self.client.get(url, data={'a': "202-12-01", 'b': '2022-12-31', 'c': 'kek'})
        self.assertEqual(response.data, 'Error 400. Bad Request: your starting_date is not suit for %Y-%m-%d')

    def test_forecast_3(self):
        url = reverse('forecast')
        response = self.client.get(url, data={'a': "2022-11-12", 'b': '202-12-10', 'c': 'black'})
        self.assertEqual(response.data, 'Error 400. Bad Request: your ending_date is not suit for %Y-%m-%d')

    def test_forecast_4(self):
        url = reverse('forecast')
        response = self.client.get(url, data={'a': "2023-01-10", 'b': '2022-02-10', 'c': 'black'})
        self.assertEqual(response.data, 'Error 400. Bad Request: starting date can not be more than ending date')

    def test_forecast_5(self):
        url = reverse('forecast')
        response = self.client.get(url, data={'a': "2022-11-10", 'b': '2022-12-10', 'c': 'lolkek'})
        self.assertEqual(response.data, 'Error 400. Bad Request: lolkek is not a valid value for color')


class HtmlScriptTest(TestCase):
    def test_gen_1(self):
        result = geneator.create_graf('2022-11-10', '2022-12-10', 'red')
        self.assertEqual(result, 'forecast.png')

    def test_gen_2(self):
        result = geneator.create_graf('202-11-10', '2022-12-10', 'red')
        self.assertEqual(result, 'your starting_date is not suit for %Y-%m-%d')

    def test_gen_3(self):
        result = geneator.create_graf('2022-11-10', '202-12-10', 'red')
        self.assertEqual(result, 'your ending_date is not suit for %Y-%m-%d')

    def test_gen_4(self):
        result = geneator.create_graf('2022-11-10', '2021-12-10', 'red')
        self.assertEqual(result, 'starting date can not be more than ending date')

    def test_gen_5(self):
        result = geneator.create_graf('2022-11-10', '2022-12-10', 'lolkek')
        self.assertEqual(result, 'lolkek is not a valid value for color')
