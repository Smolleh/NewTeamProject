from rest_framework import serializers
from .models import *

class ExhibitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exhibit
        fields = ['exhibitid', 'title', 'domain', 'backgrounddeploymentcontext', 'intededuse', 'viewnumber']
    