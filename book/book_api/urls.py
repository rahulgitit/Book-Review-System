from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from book.book_api.views import BookViewSet

# Create a router and register your viewsets
router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')

# Define the URL patterns
urlpatterns = [
    path('book/', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token)
]