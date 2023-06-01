from django.urls import path
from rest_framework.routers import DefaultRouter
from . views import BudgetEntryListCreateView, BudgetEntryRetrieveUpdateDeleteView, CategoryListCreateView, CategoryRetrieveUpdateDeleteView,BudgetEntryViewSet, CategoryViewSet

router = DefaultRouter()
router.register('user/budget-entries', BudgetEntryViewSet, basename='budget-entries')
router.register('user/categories', CategoryViewSet, basename='categories')

urlpatterns = [
    *router.urls,
    path('budget-entries/', BudgetEntryListCreateView.as_view(), name='budget-entry-list-create'),
    path('budget-entries/<int:pk>/', BudgetEntryRetrieveUpdateDeleteView.as_view(), name='budget-entry-retrieve-update-delete'),
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDeleteView.as_view(), name='category-retrieve-update-delete'),
]
