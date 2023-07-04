from django.urls import path
from .views import Homepage, Homefilmes, Detalhesfilme

app_name = 'filme'

urlpatterns = [
    # path('', homepage),
    path('', Homepage.as_view(), name='homepage'),
    path('filmes/', Homefilmes.as_view(), name='homefilmes'),
    path('filmes/<int:pk>', Detalhesfilme.as_view(), name='detalhesfilme'),
]
