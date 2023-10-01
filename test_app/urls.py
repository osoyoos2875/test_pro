#コード03
#\test_pro\test_app\urls.py

from django.urls import path
from .views import TestView

urlpatterns = [
    path(r'practice', TestView.as_view(), name='testview'),
]