from rest_framework.routers import DefaultRouter
from django.urls import path, include
from goal.views import GoalListCreateView, GoalRetrieveUpdateDeleteView, UserGoalViewSet


router = DefaultRouter()
router.register(r'api/goals/user', UserGoalViewSet, basename='user-goal')

urlpatterns = [
    path('', include(router.urls)),
    path('api/goals/', GoalListCreateView.as_view(), name='goal-list-create'),
    path('api/goals/<int:pk>/', GoalRetrieveUpdateDeleteView.as_view(), name='goal-retrieve-update-delete'),
\
]
