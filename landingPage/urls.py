from django.urls import path
from .views import AboutDetailAPIView, AboutAPIView, MissionAPIView, MissionDetailAPIView, MissionSerializer, ObjectiveAPIView, ObjectiveDetailAPIView, ObjectiveSerializer, VisionAPIView, VisionDetailAPIView, VisionSerializer

urlpatterns = [
    path('about/', AboutAPIView.as_view()),
    path('about/<int:pk>/', AboutDetailAPIView.as_view()),
    path('mission/', MissionAPIView.as_view()),
    path('mission/<int:pk>/', MissionDetailAPIView.as_view()),
    path('vision/', VisionAPIView.as_view()),
    path('vision/<int:pk>/', VisionDetailAPIView.as_view()),
    path('objective/', ObjectiveAPIView.as_view()),
    path('objective/<int:pk>/', ObjectiveDetailAPIView.as_view()),
]