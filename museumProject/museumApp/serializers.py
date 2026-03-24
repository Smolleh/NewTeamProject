from rest_framework import serializers
from .models import *



#serialises artefact objects for creation viewing and editing, keeping the exhibitID as read only so that an artefact's exhibit cannot be changed
class ArtefactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artefact
        fields = ['artefactId','info', 'artefactDate', 'artefactObjectPath']
        read_only_fields = ['exhibitId']
  
#serialises failure description objects for creation viewing and editing, keeping the exhibitID as read only so that the associated exhibit cannot be changed      
class FailureDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FailureDescription
        fields = ['failureDescriptionId','whatWentWrong', 'howItWasDetected', 'whatWasAffected']
        read_only_fields = ['exhibitId']

#serialises AI system description objects for creation viewing and editing, keeping the exhibitID as read only so that the associated exhibit cannot be changed
class AiSystemDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AiSystemDescription
        fields = ['systemDescriptionId','systemDescription', 'systemPurpose', 'systemOutputs']
        read_only_fields = ['exhibitId']

#serialises lessons learned objects for creation viewing and editing, keeping the exhibitID as read only so that the associated exhibit cannot be changed
class LessonsLearnedSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonsLearned
        fields = ['lessonslearnedId','practicalRecommendations', 'futureWarnings']
        read_only_fields = ['exhibitId']

#serialises contributing factors for creation viewing and editing, keeping the exhibitID as read only so that the associated exhibit cannot be changed
class ContributingFactorsSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = ContributingFactors
        fields = ['contributingFactorId', 'exhibitId', 'dataIssues', 'designChoices', 'organisationalOrGovernanceIssues']
        read_only_fields = ['exhibitId']
        
#curator seriaiser for creating, updating, and viewing exhibit objects. includes curator-only field viewNumber
class SimpleViewCreateExhibitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exhibit
        fields = ['exhibitId','title', 'domain','backgroundDeploymentContext', 'intededUse', 'viewNumber']
        
#visitor serialiser for displaying exhibit details along with a the first artefact's image (used when viewing all exhibits)
class SimpleViewExhibitSerializer(serializers.ModelSerializer):
    ArtefactObjectPath = serializers.SerializerMethodField()
    class Meta:
        model = Exhibit
        fields = ['exhibitId', 'title', 'domain', 'ArtefactObjectPath']

    def get_ArtefactObjectPath(self, obj):
        artefact = (
            Artefact.objects
            .filter(exhibitId=obj)               
            .order_by('artefactId')              
            .only('artefactObjectPath')
            .first()
        )
        if artefact and artefact.artefactObjectPath:
            return artefact.artefactObjectPath.name
        return None

# seriliser for detailed exhibit view, including all related models such as all artefacts, lessons learned, contributing factors, etc
class ExhibitSerializer(serializers.ModelSerializer):
    artefacts = serializers.SerializerMethodField()
    lessons_learned = LessonsLearnedSerializer(read_only=True, source="lessonslearned")
    contributing_factors = ContributingFactorsSerilaizer(read_only=True, source="contributingfactors")
    failure_description = FailureDescriptionSerializer(read_only=True, source="failuredescription")
    ai_system_description = AiSystemDescriptionSerializer(read_only=True, source="aisystemdescription")

    class Meta:
        model = Exhibit
        fields = ['exhibitId','title', 'domain','backgroundDeploymentContext', 'intededUse',
            'artefacts','lessons_learned','contributing_factors','failure_description','ai_system_description',
        ]
    def get_artefacts(self, obj):
        return ArtefactSerializer(obj.artefact_set.all(), many=True).data

#serialiser for writing comments and displaying comments on the exhibit page 
class CommentSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()

    class Meta:
        model = Comments
        fields = ['commentId', 'exhibit', 'content', 'date', 'isApproved', 'username']
        read_only_fields = ['isApproved', 'date', 'commentId']
        
    #sets the username to "Deleted User" for display if the orignal commenter has decided to delete their user account
    def get_username(self, obj):
        if obj.user is None:
            return 'Deleted User'
        return obj.user.username

#serialisers for curators to review a comment, only allowing them to change the isApproved field
class CuratorCommentReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['commentId', 'exhibit', 'content', 'date', 'isApproved']
        read_only_fields = ['exhibit', 'content', 'date']
