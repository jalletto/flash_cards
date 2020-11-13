from django.urls import path
from . import views

urlpatterns = [
    path('response', views.get_slack_response, name='get_slack_response'),
]
