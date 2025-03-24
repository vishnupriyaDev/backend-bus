from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Bus
from .serializers import BusSerializer


# GET - List all buses
@api_view(['GET'])
def bus_list(request):
    if request.method == 'GET':
        buses = Bus.objects.all()
        serializer = BusSerializer(buses, many=True)
        return Response(serializer.data)


# POST - Add a new bus
@api_view(['POST'])
def add_bus(request):
    if request.method == 'POST':
        serializer = BusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# DELETE - Delete a bus by ID
@api_view(['DELETE'])
def delete_bus(request, bus_id):
    try:
        bus = Bus.objects.get(id=bus_id)
    except Bus.DoesNotExist:
        return Response({'error': 'Bus not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        bus.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
