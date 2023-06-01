from rest_framework import generics, viewsets
from .models import Goal
from .serializers import GoalSerializer, UserGoalSerializer 


class GoalListCreateView(generics.ListCreateAPIView):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer


class GoalRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer


class UserGoalViewSet(viewsets.ModelViewSet):
    serializer_class = UserGoalSerializer

    def get_queryset(self):
        user = self.request.user
        return Goal.objects.filter(user=user) 