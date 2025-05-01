
from django.urls import path
from book import views

urlpatterns = [
    path('book_list/', views.book_list ,name="list"),
    path('book_create/', views.book_create,name="book"),
    path('book_details/<int:pk>/', views.book_details, name='detail'),
    path('book_update/<int:pk>/', views.book_update, name='update'),
    path('book_delete/<int:pk>/', views.book_delete, name='delete'),
    path('search/', views.search, name="search"),



]
