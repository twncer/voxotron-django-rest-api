from rest_framework import serializers
from . import models

class CampusStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CampusStudent
        fields = '__all__'