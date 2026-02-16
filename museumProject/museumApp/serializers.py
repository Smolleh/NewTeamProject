from rest_framework import serializers
from .models import *




class ArtefactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artefact
        fields = ['artefactId','info', 'artefactDate', 'artefactObjectPath']
        read_only_fields = ['exhibitId']
        
class FailureDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FailureDescription
        fields = ['failureDescriptionId','whatWentWrong', 'howItWasDetected', 'whatWasAffected']
        read_only_fields = ['exhibitId']

class AiSystemDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AiSystemDescription
        fields = ['systemDescriptionId','systemDescription', 'systemPurpose', 'systemOutputs']
        read_only_fields = ['exhibitId']


class LessonsLearnedSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonsLearned
        fields = ['lessonslearnedId','practicalRecommendations', 'futureWarnings']
        read_only_fields = ['exhibitId']


class ContributingFactorsSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = ContributingFactors
        fields = ['contributingFactorId', 'exhibitId', 'dataIssues', 'designChoices', 'organisationalOrGovernanceIssues']
        read_only_fields = ['exhibitId']
        
class SimpleViewCreateExhibitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exhibit
        fields = ['exhibitId','title', 'domain','backgroundDeploymentContext', 'intededUse', 'viewNumber']
class SimpleViewExhibitSerializer(serializers.ModelSerializer):
    ArtefactObjectPath = serializers.SerializerMethodField()
    class Meta:
        model = Exhibit
        fields = ['exhibitId', 'title', 'domain', 'viewNumber', 'ArtefactObjectPath']

    def get_ArtefactObjectPath(self, obj):
        artefact = (
            Artefact.objects
            .filter(exhibitId=obj)               
            .order_by('artefactId')              
            .only('artefactObjectPath')
            .first()
        )
        return artefact.artefactObjectPath if artefact else None
    
class ExhibitSerializer(serializers.ModelSerializer):
    artefacts = ArtefactSerializer(read_only=True, source="artefact")
    lessons_learned = LessonsLearnedSerializer(read_only=True, source="lessonslearned")
    contributing_factors = ContributingFactorsSerilaizer(read_only=True, source="contributingfactors")
    failure_description = FailureDescriptionSerializer(read_only=True, source="failuredescription")
    ai_system_description = AiSystemDescriptionSerializer(read_only=True, source="aisystemdescription")

    class Meta:
        model = Exhibit
        fields = ['exhibitId','title', 'domain','backgroundDeploymentContext', 'intededUse',
            'viewNumber','artefacts','lessons_learned','contributing_factors','failure_description','ai_system_description',
        ]