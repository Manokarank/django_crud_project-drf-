from django.urls import path
from .views import CandidateList, CandidateDetail, candidate_list

urlpatterns = [
    path('api/candidateslist/', CandidateList.as_view(), name='candidate-list-api'),
    path('api/candidates/<int:pk>/', CandidateDetail.as_view(), name='candidate-detail-api'),
    path('api/candidates/', candidate_list, name='candidate-list'),

]
