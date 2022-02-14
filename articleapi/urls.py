from django.urls import path,include
from rest_framework import routers
from .views import ArticleApiView
router = routers.DefaultRouter()

# router.register(r'articles',ArticleViewSet)

urlpatterns = [
    # path('',include(router.urls)),
    path('article/',ArticleApiView.as_view(),name = "article"),
    path('article/<int:pk>/',ArticleApiView.as_view(),name="uniquearticle")
]
