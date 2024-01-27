from django.urls import path
from core.views import HomePageView, SampleView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("", SampleView.as_view(), name="sample"),
]