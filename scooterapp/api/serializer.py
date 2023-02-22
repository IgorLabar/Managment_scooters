from rest_framework import serializers
from scooter_api.models import Scooter, Trip, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'city', 'email', 'first_name', 'last_name',)


class ScooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scooter
        fields = '__all__'


class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'