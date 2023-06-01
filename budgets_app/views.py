from rest_framework import viewsets, generics
from .models import BudgetEntry, Category
from .serializers import (BudgetEntrySerializer, CategorySerializer,
                           BudgetEntryRetrieveSerializer, CategoryRetrieveSerializer)



class BudgetEntryListCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = BudgetEntry.objects.all()
    serializer_class = BudgetEntrySerializer


class BudgetEntryRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests for the BudgetEntry model."""
    queryset = BudgetEntry.objects.all()
    serializer_class = BudgetEntrySerializer

class BudgetEntryViewSet(viewsets.ReadOnlyModelViewSet):
    """This class handles the http GET, PUT and DELETE requests 
    for the BudgetEntry model foraa spcific user."""
    serializer_class = BudgetEntryRetrieveSerializer
    allowed_methods = ['GET', 'PUT', 'DELETE']

    def get_queryset(self):
        user = self.request.user
        return BudgetEntry.objects.filter(user=user)

class CategoryListCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CategoryRetrieveSerializer

    def get_queryset(self):
        user = self.request.user
        return Category.objects.filter(user=user)
    