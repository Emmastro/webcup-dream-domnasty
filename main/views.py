from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from main import models, serializers
from .utils import get_chatgpt_dream_assessment
# from accounts.models import Client

class DreamViewSet(viewsets.ModelViewSet):
    queryset = models.Dream.objects.all()
    serializer_class = serializers.DreamSerializer

    @action(detail=False, methods=['get'])
    def get_dreams(self, request):
        dreams = models.Dream.objects.all()
        serializer = self.serializer_class(dreams, many=True)
        return Response(serializer.data)



    def perform_create(self, serializer):
        
        dream = serializer.validated_data['dream']
        assessment = get_chatgpt_dream_assessment(dream)
        print("usern id: ", self.request.user)

        serializer.save(assessment=assessment, client=self.request.user)