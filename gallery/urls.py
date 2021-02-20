from django.urls import path
from .views import (GalleryHome, AddImageView, DeleteImageView)


urlpatterns = [

    path('', GalleryHome.as_view(), name='gallery_home'),

    path('images/', AddImageView.as_view(), name='add_image'),

    path('images/<int:pk>/', DeleteImageView.as_view(), name='delete_image'),

]
