from django.shortcuts import render
from django.db.models import Count
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models, serializers

# Create your views here.

def index_view(request):
    return render(request, 'index.html', {})

@api_view(['GET'])
def VoteForVoxotron(request, intra_name, vote):
    vote_for = models.CampusStudent.objects.filter(username = vote)
    if not vote_for.exists():
        return Response({'response': 'VOTE_NOT_EXISTS'})
    voter = models.CampusStudent.objects.filter(username = intra_name)
    if not voter.exists():
        return Response({'response': 'VOTER_NOT_EXISTS'})
    if models.VoxotronForm.objects.filter(voter = intra_name, vote = vote_for[0]).exists():
        return Response({'response': 'VOTE_ALREADY_EXISTS'})
    if models.VoxotronForm.objects.filter(voter = intra_name).count() == 3:
        return Response({'response': 'STUDENT_VOTED_LIMIT'})
    try:
        vote = models.VoxotronForm.objects.create(vote = vote_for[0], voter = intra_name)
    except:
        return Response({'response': 'DJANGO_ERROR'})
    if not vote.id:
        return Response({'response': 'FAILED_TO_VOTE'})
    return Response({'response': 'OK'})

@api_view(['GET'])
def FetchCampusStudents(request):
    students = models.CampusStudent.objects.annotate(vote_count=Count('voxotronform')).order_by('-vote_count')
    serializer = serializers.CampusStudentSerializer(students, many = True)
    return Response(serializer.data)