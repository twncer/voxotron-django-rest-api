from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index_view),
    path('api/new-vote/<intra_name>/<vote>', views.VoteForVoxotron, name = "name?=vote_for_voxotron"),
    path('api/serializers/campusstudent', views.FetchCampusStudents, name = "name?=fetch_campus_students"),
    
]
