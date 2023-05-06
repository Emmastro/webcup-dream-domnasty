from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from main import models, serializers

class DreamViewSet(viewsets.ModelViewSet):
    queryset = models.Dream.objects.all()
    serializer_class = serializers.DreamSerializer

    @action(detail=False, methods=['get'])
    def get_dreams(self, request):
        dreams = models.Dream.objects.all()
        serializer = self.serializer_class(dreams, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def get_dreams_by_client(self, request):
        client = request.user
        dreams = models.Dream.objects.filter(client=client)
        serializer = self.serializer_class(dreams, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def get_dreams_by_client_and_date(self, request):
        client = request.user
        date = request.GET.get('date')
        dreams = models.Dream.objects.filter(client=client, dream_date=date)
        serializer = self.serializer_class(dreams, many=True)
        return Response(serializer.data)

