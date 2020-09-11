from django.shortcuts import render
from showmgmt.models import Movie, Show, Cinema
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.response import Response
from rest_framework import status
from .models import Booking
from .serializers import BookingSerializer

class BookShowView(APIView):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        post_data = request.POST
        show = post_data.get('show_id')     
        reserved_seat_count = post_data.get('seat_count')
        user = request.user.id
        print(request.user.id)
        data = {}
        data['user'] = user
        data['show'] = show
        data['reserved_seat_count'] = reserved_seat_count

        try:
            show_obj = Show.objects.get(id=show)
        except:
            return Response({"error": "Invalid show ID"}, status=status.HTTP_400_BAD_REQUEST)
        serializer =  BookingSerializer(data=data)
        if serializer.is_valid():
            if int(reserved_seat_count) == 0:
                return Response({"error": "Atleast 1 seat to be booked"}, status=status.HTTP_400_BAD_REQUEST)
            elif int(reserved_seat_count) > show_obj.seat_available:
                return Response({"error": "Requested number of seat(s) not avaialble"}, status=status.HTTP_400_BAD_REQUEST)
            booking = serializer.save()
            return Response({"booking_id": booking.booking_id, "seats_reserved": booking.reserved_seat_count}, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response({"error": "Invalid request"}, status=status.HTTP_400_BAD_REQUEST)
