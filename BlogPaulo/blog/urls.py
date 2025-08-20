from django.urls import path
from .views import (
    home, about,
    PageListView, PageDetailView, PageCreateView, PageUpdateView, PageDeleteView,
)

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('pages/', PageListView.as_view(), name='page-list'),
    path('pages/<int:pk>/', PageDetailView.as_view(), name='page-detail'),
    path('pages/create/', PageCreateView.as_view(), name='page-create'),
    path('pages/<int:pk>/update/', PageUpdateView.as_view(), name='page-update'),
    path('pages/<int:pk>/delete/', PageDeleteView.as_view(), name='page-delete'),
]
