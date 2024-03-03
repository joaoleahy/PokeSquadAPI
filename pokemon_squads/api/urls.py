from django.urls import path
from .views import TeamListView, TeamCreateView

urlpatterns = [
    path('teams/', TeamListView.as_view(), name='team-list'),
    path('teams/create/', TeamCreateView.as_view(), name='team-create'),
]
