from django.urls import path
from .views import BlogCreate, BlogDetails, BlogList, BlogUpdate, BlogDelete, TagDetails

urlpatterns = [
    path('create/', BlogCreate.as_view(), name='create'),
    path('details/<int:pk>/', BlogDetails.as_view(), name='blog-details'),
    path('blogs/', BlogList.as_view(), name='blogs'),
    path('update/<int:pk>/', BlogUpdate.as_view(), name='blog-update'),
    path('delete/<int:pk>/', BlogDelete.as_view(), name='blog-delete'),
    path('tag/<int:pk>/', TagDetails.as_view(), name='tag-details'),
]