from rest_framework import serializers
from .models import *

class ExhibitSerializer(serializers.ModelSerializer):
    first_artefact = serializers.SerializerMethodField()

    class Meta:
        model = Exhibit
        fields = ['exhibitid', 'title', 'domain', 'backgrounddeploymentcontext', 'intededuse', 'viewnumber','first_artefact']

    def get_first_artefact(self, obj):
        artefact = (Artefact.objects.filter(exhibitid=obj.exhibitid).order_by('artefactid').first()
        )
        if artefact is None:
            return None
        
        else:
            return ArtefactSerializer(artefact).data

    
class ArtefactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artefact
        fields = ['artefactid','info', 'artefactdate', 'artefactobjectpath', 'exhibitid']