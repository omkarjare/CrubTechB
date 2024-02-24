from django.urls import path
from .views import *


urlpatterns = [
    path('ov/', order_view, name='order_url'),
    path('sv/', show_view, name='show_url'),
    path('uv/<int:pk>/', update_view, name='update_url'),
    path('dv/<int:pk>/', delete_view, name='delete_url')
]