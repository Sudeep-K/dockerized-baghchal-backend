from django.urls import path
from . import views

urlpatterns = [
    path("api/v1/best-move", views.get_best_move, name="get_best_move"),
]
