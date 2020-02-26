from django.urls import path

from .views import MsgAPIController

urlpattern = [
    path('messages', MsgAPIController.as_view()),
]