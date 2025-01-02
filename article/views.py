from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from article.models import Article, Category, Tag, Avatar
from article.serializers import ArticleSerializer, ArticleDetailSerializer, CategorySerializer, TagSerializer, AvatarSerializer,UserSerializer
from article.permissions import IsOwnerOrReadOnly,IsAuthenticated
from rest_framework import filters
from django.contrib.auth.models import User




class AvatarViewSet(viewsets.ModelViewSet):
    queryset = Avatar.objects.all()
    serializer_class = AvatarSerializer
    permission_classes = [IsOwnerOrReadOnly]

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsOwnerOrReadOnly]
    pagination_class = None

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsOwnerOrReadOnly]
    pagination_class = None
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)  # 设置 author 字段


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    #permission_classes = [IsOwnerOrReadOnly]
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_serializer_class(self):
        if self.action in ['list', 'create']:
            return ArticleSerializer
        return ArticleDetailSerializer

    filterset_fields = ['author__username', 'title']

    def get_queryset(self):
        queryset = self.queryset
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(author__username=username)
        return queryset

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsOwnerOrReadOnly]