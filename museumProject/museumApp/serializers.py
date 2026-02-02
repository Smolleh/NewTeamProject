from rest_framework import serializers
from .models import *

class ExhibitSerializer(serializers.ModelSerializer):
    first_artefact = serializers.SerializerMethodField()

    class Meta:
        model = Exhibit
        fields = ['exhibitId', 'title', 'domain', 'backgroundDeploymentContext', 'intededUse', 'viewNumber','first_artefact']

    def get_first_artefact(self, obj):
        artefact = (Artefact.objects.filter(exhibitId=obj.exhibitId).order_by('artefactId').first()
        )
        if artefact is None:
            return None
        
        else:
            return ArtefactSerializer(artefact).data

    
class ArtefactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artefact
        fields = ['artefactId','info', 'artefactDate', 'artefactObjectPath', 'exhibitId']
        
class FailureDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FailureDescription
        fields = ['failureDescriptionId', 'exhibitId', 'whatWentWrong', 'whatWasAffected'] 




class LessonsLearnedSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonsLearned
        fields = ['lessonsLearnedId', 'exhibitId', 'practicalRecommendations', 'futureWarnings']
    
class AiSystemDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AiSystemDescription
        fields = ['systemDescriptionId', 'exhibitId', 'systemDescription', 'systemPurpose','systemOutputs',]