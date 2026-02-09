from django.db import models
##cammelcase exhibitId eg not ExhibitID or exhibitid 
class Exhibit(models.Model):
    exhibitId = models.AutoField(db_column='exhibitId', primary_key=True)  
    title = models.TextField(db_column='title', blank=True, null=True) 
    domain = models.TextField(db_column='domain', blank=True, null=True)  
    backgroundDeploymentContext = models.TextField(db_column='backgroundDeploymentContext', blank=True, null=True) 
    intededUse = models.TextField(db_column='intededUse', blank=True, null=True) 
    viewNumber = models.IntegerField(db_column='viewNumber', blank=True, null=True)  

class Quizzes(models.Model):
    quizId = models.AutoField(db_column='quizId', primary_key=True, blank=True, null=False)   
    exhibitId = models.ForeignKey(Exhibit, models.CASCADE, db_column='exhibitId', blank=True, null=True)   
    quizzDetails = models.TextField(db_column='quizzDetails', blank=True, null=True)   
    completionRate = models.IntegerField(db_column='completionRate', blank=True, null=True)   
    attemptRate = models.IntegerField(db_column='attemptRate', blank=True, null=True)   
    totalQuestionPoints = models.IntegerField(db_column='totalQuestionPoints', blank=True, null=True)   

    class Meta:
        managed = False
        db_table = 'quizzes'

class Artefact(models.Model):
    artefactId = models.AutoField(db_column='artefactId', primary_key=True)  
    info = models.CharField(db_column='info', blank=True, null=True)  
    artefactDate = models.DateField(db_column='artefactDate', blank=True, null=True)  
    artefactObjectPath = models.ImageField(db_column='artefactObjectPath',  null=True,upload_to='museumProject/museumApp/ArtefactImages/')  
    exhibitId = models.ForeignKey(Exhibit, models.CASCADE, db_column='exhibitId')  

class Users(models.Model):
    userId = models.AutoField(db_column='userId', primary_key=True, blank=True, null=False)   
    userLevel = models.IntegerField(db_column='userLevel')   
    fName = models.CharField(db_column='fName', blank=True, null=True)   
    lName = models.CharField(db_column='lName', blank=True, null=True)  
    password = models.CharField(db_column='password', blank=True, null=True)  
    totalQuizzPoints = models.IntegerField(db_column='totalQuizzPoints', blank=True, null=True) 

    class Meta:
        managed = False
        db_table = 'users'

class AiSystemDescription(models.Model):
    systemDescriptionId = models.AutoField(db_column='systemDescriptionId', primary_key=True, null=False)   
    exhibitId = models.ForeignKey(Exhibit, models.CASCADE, db_column='exhibitId', blank=True, null=True)   
    systemDescription = models.TextField(db_column='systemDescription', blank=True, null=True)   
    systemPurpose = models.TextField(db_column='systemPurpose', blank=True, null=True)   
    systemOutputs = models.TextField(db_column='systemOutputs', blank=True, null=True)   

    class Meta:
        managed = True
        db_table = 'AI_system_description'





class AttemptedQuizzes(models.Model):
    pk = models.CompositePrimaryKey('userId', 'quizId')
    userId = models.ForeignKey(Users, models.CASCADE, db_column='userId', blank=True, null=False)   
    quizId = models.ForeignKey(Quizzes, models.CASCADE, db_column='quizId', blank=True, null=False)   
    pointsGained = models.IntegerField(db_column='pointsGained', blank=True, null=True)   
    attemptDate = models.DateField(db_column='attemptDate', blank=True, null=True)   

    class Meta:
        managed = False
        db_table = 'attempted_quizzes'



"""
class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


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


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)

"""

class BookMarks(models.Model):
    pk = models.CompositePrimaryKey('userId', 'exhibitId')
    userId = models.ForeignKey(Users, models.CASCADE, db_column='userId', blank=True, null=False)   
    exhibitId = models.ForeignKey(Exhibit, models.CASCADE, db_column='exhibitId', blank=True, null=False)   

    class Meta:
        managed = False
        db_table = 'book_marks'



class ContributingFactors(models.Model):
    contributingFactorId = models.AutoField(db_column='contributingFactorId', primary_key=True, blank=True, null=False)   
    exhibitId = models.ForeignKey(Exhibit, models.CASCADE , db_column='exhibitId', blank=True, null=True)   
    dataIssues = models.TextField(db_column='dataIssues', blank=True, null=True)   
    designChoices = models.TextField(db_column='designChoices', blank=True, null=True)   
    organisationalOrGovernanceIssues = models.TextField(db_column='organisationalOrGovernanceIssues', blank=True, null=True)   

    class Meta:
        managed = True
        db_table = 'contributing_factors'

"""
class DjangoAdminLog(models.Model):
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'







"""
class FailureDescription(models.Model):
    failureDescriptioniId = models.AutoField(db_column='failureDescriptionId', primary_key=True, null=False)   
    exhibitId = models.ForeignKey(Exhibit, models.CASCADE, db_column='exhibitId', blank=True, null=True)   
    whatWentWrong = models.TextField(db_column='whatWentWrong', blank=True, null=True)   
    howItWasDetected = models.TextField(db_column='howItWasDetected', blank=True, null=True)   
    whatWasAffected = models.TextField(db_column='whatWasAffected', blank=True, null=True)   

    class Meta:
        managed = True
        db_table = 'failure_description'


class LessonsLearned(models.Model):
    lessonslearnedId = models.AutoField(db_column='lessonsLearnedId', primary_key=True, blank=True, null=False)   
    exhibitId = models.ForeignKey(Exhibit, models.CASCADE, db_column='exhibitId', blank=True, null=True)   
    practicalRecommendations = models.TextField(db_column='practicalRecommendations', blank=True, null=True)   
    futureWarnings = models.TextField(db_column='futureWarnings', blank=True, null=True)   

    class Meta:
        managed = True
        db_table = 'lessons_learned'







class QuizzQuestions(models.Model):
    questionId = models.AutoField(db_column='questionId', primary_key=True, blank=True, null=False)   
    quizId = models.ForeignKey(Quizzes, models.CASCADE, db_column='quizId', blank=True, null=True)   
    question = models.TextField(db_column='question')
    option1 =  models.TextField(db_column='option1')  
    option2 = models.TextField(db_column='option2')
    option3 = models.TextField(db_column='option3')
    option4 = models.TextField(db_column='option4')
    questionAnswer = models.IntegerField(db_column='questionAnswer')   
    completionRate = models.IntegerField(db_column='completionRate', blank=True, null=True)   
    attemptRate = models.IntegerField(db_column='attemptRate', blank=True, null=True)   
    points = models.IntegerField(db_column='points', blank=True, null=True)   

    class Meta:
        managed = False
        db_table = 'quizz_questions'
        


