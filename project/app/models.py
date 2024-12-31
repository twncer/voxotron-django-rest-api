from django.db import models
from datetime import datetime

# Create your models here.

voxotroners = [
    ("1", "btuncer"),
    ("2", "husarpka"),
    ("3", "reren"),
    ("4", "yuocak"),
    ("5", "merilhan"),
    ("6", "tuzan"),
    ("7", "muokcan"),
    ("8", "duslu"),
    ("9", "saincesu")
]

class CampusStudent(models.Model):
    username = models.CharField(max_length = 67, unique = True)
    is_active = models.BooleanField(default = True)

    def __str__(self):
        return self.username

class VoxotronForm(models.Model):
    vote = models.ForeignKey(CampusStudent, on_delete = models.CASCADE)
    voter = models.CharField(max_length = 67)
    vote_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.voter} => {self.vote.username}"