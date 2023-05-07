from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from main import models, serializers
from .utils import get_chatgpt_dream_assessment
# from accounts.models import Client


class DreamViewSet(viewsets.ModelViewSet):
    queryset = models.Dream.objects.all()
    serializer_class = serializers.DreamSerializer

    @action(detail=False, methods=['get'])
    def get_dreams(self, request):
        dreams = models.Dream.objects.filter(client=self.request.user)
        serializer = self.serializer_class(dreams, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):

        dream = serializer.validated_data['dream']
        assessment = get_chatgpt_dream_assessment(dream)
        print("usern id: ", self.request.user)

        serializer.save(assessment=assessment, client=self.request.user)

class PostViewSet(viewsets.ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer

    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # TODO: restrict only admin can create posts
        if self.request.user.is_staff:
            serializer.save(author=self.request.user)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


class ContactViewSet(viewsets.ModelViewSet):
    queryset = models.Contact.objects.all()
    serializer_class = serializers.ContactSerializer


