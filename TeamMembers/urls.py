from django.urls import path
from . import views
from django.conf import settings


urlpatterns = [
path('agents/', views.Agents, name = "agents"),
path('agents/add/', views.AddAgent, name = "add agent"),
path('agents/<int:agent_id>/', views.AgentInfo, name = "agent info"),
path('agents/<int:agent_id>/requested/', views.requested, name = "requested by agent"),
path('agents/<int:agent_id>/pendings/', views.pendings, name = "pending requests"),
path('agents/<int:agent_id>/completed/', views.completed, name = "completed requests")
]