from django.urls import path

from . import views

urlpatterns = [
    path('', views.index,name="test"),
    
    path('upload/', views.upload_wav_file,name="upload"),
]
