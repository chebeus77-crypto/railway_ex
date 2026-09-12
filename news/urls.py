from django.urls import path

from . import views

urlpatterns = [
    path('', views.NewsSearchView.as_view(), name='news-search'),
]
