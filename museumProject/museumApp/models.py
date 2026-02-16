from django.db import models
##cammelcase exhibitId eg not ExhibitID or exhibitid 
# very important to use column name same as varaible name
# everything except primary key should be blank = True, null = True

class Exhibit(models.Model):
    exhibitId = models.AutoField(db_column='exhibitId', primary_key=True)  
    title = models.TextField(db_column='title', blank=True, null=False) 
    domain = models.TextField(db_column='domain', blank=True, null=False)  
    backgroundDeploymentContext = models.TextField(db_column='backgroundDeploymentContext', blank=True, null=False) 
    intededUse = models.TextField(db_column='intededUse', blank=True, null=False) 
    viewNumber = models.IntegerField(db_column='viewNumber', blank=True, null=False)  
    def __str__(self):
        return str(self.title)



class Artefact(models.Model):
    artefactId = models.AutoField(db_column='artefactId', primary_key=True)  
    info = models.CharField(db_column='info', max_length=255, blank=True, null=False)  
    artefactDate = models.DateField(db_column='artefactDate', blank=True, null=False)  
    artefactObjectPath = models.TextField(db_column='artefactObjectPath', blank=True, null=False)  
    exhibitId = models.ForeignKey(Exhibit, models.CASCADE, db_column='exhibitId')  


class AiSystemDescription(models.Model):
    systemDescriptionId = models.AutoField(db_column='systemDescriptionId', primary_key=True, null=False)   
    exhibitId = models.ForeignKey(Exhibit, on_delete=models.CASCADE,db_column='exhibitId', blank= True, null = True)
    systemDescription = models.TextField(db_column='systemDescription', blank=True, null=True)   
    systemPurpose = models.TextField(db_column='systemPurpose', blank=True, null=True)   
    systemOutputs = models.TextField(db_column='systemOutputs', blank=True, null=True)   

    class Meta:
        managed = True
        db_table = 'AI_system_description'

class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class BookMarks(models.Model):
    pk = models.CompositePrimaryKey('userId', 'exhibitId')
    userId = models.ForeignKey(AuthUser, models.CASCADE, db_column='userId', blank=True, null=False)   
    exhibitId = models.ForeignKey(Exhibit, models.CASCADE, db_column='exhibitId', blank=True, null=False)   

    class Meta:
        managed = False
        db_table = 'book_marks'



class ContributingFactors(models.Model):
    contributingFactorId = models.AutoField(db_column='contributingFactorId', primary_key=True, blank=True, null=False)   
    exhibitId = models.ForeignKey(Exhibit, models.CASCADE , db_column='exhibitId', blank=True, null=False)   
    dataIssues = models.TextField(db_column='dataIssues', blank=True, null=False)   
    designChoices = models.TextField(db_column='designChoices', blank=True, null=False)   
    organisationalOrGovernanceIssues = models.TextField(db_column='organisationalOrGovernanceIssues', blank=True, null=False)   

    class Meta:
        managed = True
        db_table = 'contributing_factors'


class FailureDescription(models.Model):
    failureDescriptioniId = models.AutoField(db_column='failureDescriptionId', primary_key=True, null=False)   
    exhibit = models.OneToOneField(Exhibit, on_delete=models.CASCADE,related_name='failureDescription', null=True, blank= True)
    whatWentWrong = models.TextField(db_column='whatWentWrong', blank=True, null=False)   
    howItWasDetected = models.TextField(db_column='howItWasDetected', blank=True, null=False)   
    whatWasAffected = models.TextField(db_column='whatWasAffected', blank=True, null=False)   

    class Meta:
        managed = True
        db_table = 'failure_description'


class LessonsLearned(models.Model):
    lessonslearnedId = models.AutoField(db_column='lessonsLearnedId', primary_key=True, blank=True, null=False)   
    exhibitId = models.ForeignKey(Exhibit, models.CASCADE, db_column='exhibitId', blank=True, null=False)   
    practicalRecommendations = models.TextField(db_column='practicalRecommendations', blank=True, null=False)   
    futureWarnings = models.TextField(db_column='futureWarnings', blank=True, null=False)   

    class Meta:
        managed = True
        db_table = 'lessons_learned'



