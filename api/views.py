from django.shortcuts import render
from django.http import JsonResponse

from .serializers import CandidateSerializer
from .models import Candidate

def candidate_list(request):
   candidates = Candidate.objects.all()
   serializer = CandidateSerializer(candidates, many=True)
 
   return JsonResponse({'data': serializer.data})
