from django.shortcuts import render
from rest_framework import generics
from .models import Candidates
from .serializers import CandidateSerializer

class CandidateList(generics.ListCreateAPIView):
    queryset = Candidates.objects.all()
    serializer_class = CandidateSerializer

class CandidateDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Candidates.objects.all()
    serializer_class = CandidateSerializer
    
def candidate_list(request):
    candidate = Candidates.objects.all()
    return render(request, 'candidate_list.html', {'candidates': candidate})
    