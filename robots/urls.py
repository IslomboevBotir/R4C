from django.urls import path

from robots import views

urlpatterns = [
    path("report-excel/", views.RobotsInfoReportExcel.as_view())
]
