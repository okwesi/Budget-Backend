from django.urls import path
from .views import ReportListCreateView, ReportRetrieveUpdateDeleteView

urlpatterns = [
    path('api/reports/', ReportListCreateView.as_view(), name='report-list-create'),
    path('api/reports/<int:pk>/', ReportRetrieveUpdateDeleteView.as_view(), name='report-retrieve-update-delete'),
]
