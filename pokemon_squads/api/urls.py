from django.urls import path
from .views import TeamListView, TeamRetrieveView, TeamCreateView

urlpatterns = [
    path('teams/', TeamListView.as_view(), name='team-list'),
    path('teams/create/', TeamCreateView.as_view(), name='team-create'),
    path('api/teams/<str:user>/', TeamRetrieveView.as_view(), name='retrieve-team'),
]
