from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from main import models, serializers
from .utils import get_chatgpt_dream_assessment
from django.contrib.auth.models import User


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
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def get_dream_by_id(self, request):
        id = request.query_params.get('id')
        dream = models.Dream.objects.filter(id=id)
        serializer = self.serializer_class(dream, many=True)
        return Response(serializer.data)

class PostViewSet(viewsets.ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer

    #permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # TODO: restrict only admin can create posts
        # if self.request.user.is_staff:
        user = User.objects.get(username=self.request.user)
        serializer.save(author=user)
        return Response(serializer.data)
        # else:
        #     return Response(status=status.HTTP_401_UNAUTHORIZED)

    @action(detail=False, methods=['get'])
    def get_posts(self, request):
        posts = models.Post.objects.all()
        print("posts: ", posts)
        serializer = self.serializer_class(posts, many=True)
        return Response(serializer.data)
    
class ContactViewSet(viewsets.ModelViewSet):
    queryset = models.Contact.objects.all()
    serializer_class = serializers.ContactSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
