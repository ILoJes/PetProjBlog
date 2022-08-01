from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('posts/',
         views.SubjectListView.as_view(),
         name='subject_list'),

    path('posts/<pk>/',
         views.SubjectDetailView.as_view(),
         name='subject_detail'),
]
