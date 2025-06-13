from django.urls import path
from .views import inbox, message_detail, send_message

urlpatterns = [
    path('', inbox, name='inbox'),
    path('send/', send_message, name='send_message'),
    path('<int:pk>/', message_detail, name='message_detail'),
]
