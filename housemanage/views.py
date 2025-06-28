from .serializers import OwnerSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import Owner
from django.shortcuts import get_object_or_404  # Better than .get() with no try/except


@api_view(['POST'])
def create_owner(request):
    serializer = OwnerSerializer(data=request.data)  
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)  
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_owners(request):
    owner_data = Owner.objects.all()  
    serializer = OwnerSerializer(owner_data, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK) 


@api_view(['PUT'])
def update_owner(request, id):
    owner_data = get_object_or_404(Owner, id=id)
    serializer = OwnerSerializer(owner_data, data=request.data)  
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_specific_owner(request, id):
    owner_data = get_object_or_404(Owner, id=id)
    serializer = OwnerSerializer(owner_data)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['DELETE'])
def delete_owner(request, id):
    owner_data = get_object_or_404(Owner, id=id)
    owner_data.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
