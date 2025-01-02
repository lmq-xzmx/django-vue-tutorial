from django.urls import path, include
from rest_framework.routers import DefaultRouter
from article import views


app_name = 'article'

router = DefaultRouter()
router.register(r'articles', views.ArticleViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'tags', views.TagViewSet)
router.register(r'avatars', views.AvatarViewSet)
router.register(r'user', views.UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    
]
