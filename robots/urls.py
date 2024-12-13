from django.urls import path

from robots import views

urlpatterns = [
    path("", views.RobotsView.as_view())
]
