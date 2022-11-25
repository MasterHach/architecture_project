from rest_framework import serializers


class ForecastingSerializers(serializers.Serializer):
    first_date = serializers.DateTimeField()
    last_date = serializers.DateTimeField()
    color = serializers.CharField()
    file_way = serializers.CharField()
