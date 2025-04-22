from django.urls import path
from . import views

urlpatterns = [
    path('', views.topic_input_view, name='topic_input'),
    path('layer2/', views.layer2_view, name='layer2'),
    path('layer3/', views.layer3_view, name='layer3'),
    path('layer4/', views.layer4_view, name='layer4'),
    path('layer5/', views.layer5_view, name='layer5'),
    path('layer6/', views.layer6_view, name='layer6'),
    path('layer7/', views.layer7_view, name='layer7'),
    
]
