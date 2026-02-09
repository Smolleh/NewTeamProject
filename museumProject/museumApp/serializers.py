from rest_framework import serializers
from .models import *



    
class ArtefactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artefact
        fields = ['info', 'artefactDate', 'artefactObjectPath']
        
class FailureDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FailureDescription
        fields = ['whatWentWrong', 'howItWasDetected', 'whatWasAffected']

class AiSystemDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AiSystemDescription
        fields = ['systemDescription', 'systemPurpose', 'systemOutputs']



class LessonsLearnedSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonsLearned
        fields = ['practicalRecommendations', 'futureWarnings']

        

class ContributingFactorsSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = ContributingFactors
        fields = ['contributingFactorId', 'exhibitId', 'dataIssues', 'designChoices', 'organisationalOrGovernanceIssues']

class ExhibitSerializer(serializers.ModelSerializer):
    artefacts = serializers.SerializerMethodField()
    lessons_learned = serializers.SerializerMethodField()
    contributing_factors = serializers.SerializerMethodField()
    failure_description = FailureDescriptionSerializer(read_only=True, source="failureDescription")
    ai_system_description = AiSystemDescriptionSerializer(read_only=True, source="systemDescription")

    class Meta:
        model = Exhibit
        fields = [
            'exhibitId',
            'title',
            'domain',
            'backgroundDeploymentContext',
            'intededUse',
            'viewNumber',
            'artefacts',
            'lessons_learned',
            'contributing_factors',
            'failure_description',
            'ai_system_description',
        ]

    def get_artefacts(self, obj):
        return ArtefactSerializer(
            obj.artefact_set.all(), many=True
        ).data

    def get_lessons_learned(self, obj):
        return LessonsLearnedSerializer(
            obj.lessonslearned_set.all(), many=True
        ).data

    def get_contributing_factors(self, obj):
        return ContributingFactorsSerilaizer(
            obj.contributingfactors_set.all(), many=True
        ).data