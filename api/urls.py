from django.conf.urls import url
from .views import TimestampAPIView

urlpatterns = [
    url(r'^', TimestampAPIView.as_view()),
]
