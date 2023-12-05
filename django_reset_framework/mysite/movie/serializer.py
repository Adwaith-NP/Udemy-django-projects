from rest_framework import serializers
from .models import Moviedata

class Movieserializer(serializers.ModelSerializer):
    class Meta:
        img = serializers.ImageField(max_length = None,use_url = True)
        model = Moviedata
        fields = ['pk','name','duration','rating','typ','img']