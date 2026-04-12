from django.urls import path
from .views import recommend    #test_openai

urlpatterns = [
    path('recommend/', recommend),
    # path("test/", test_openai),
]