from api.serializer import UserSerializer, ScooterSerializer, TripSerializer
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from scooter_api.models import Scooter, Trip, User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser


class UserViewList(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class ScooterViewList(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        scooters = Scooter.objects.all()
        serializer = ScooterSerializer(scooters, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ScooterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class ScooterApi(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Scooter.objects.all()
    serializer_class = ScooterSerializer


class TripViewList(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        trips = Trip.objects.all()
        serializer = TripSerializer(trips, many=True)
        return Response(serializer.data)