from django.db import models
##cammelcase exhibitId eg not ExhibitID or exhibitid 
class Exhibit(models.Model):
    exhibitId = models.AutoField(db_column='exhibitId', primary_key=True)  
    title = models.TextField(db_column='title', blank=True, null=False) 
    domain = models.TextField(db_column='domain', blank=True, null=False)  
    backgroundDeploymentContext = models.TextField(db_column='backgroundDeploymentContext', blank=True, null=False) 
    intededUse = models.TextField(db_column='intededUse', blank=True, null=False) 
    viewNumber = models.IntegerField(db_column='viewNumber', blank=True, null=False)  

class Quizzes(models.Model):
    quizId = models.AutoField(db_column='quizId', primary_key=True, blank=True, null=False)   
    exhibitId = models.ForeignKey(Exhibit, models.CASCADE, db_column='exhibitId', blank=True, null=False)   
    quizzDetails = models.TextField(db_column='quizzDetails', blank=True, null=False)   
    completionRate = models.IntegerField(db_column='completionRate', blank=True, null=False)   
    attemptRate = models.IntegerField(db_column='attemptRate', blank=True, null=False)   
    totalQuestionPoints = models.IntegerField(db_column='totalQuestionPoints', blank=True, null=False)   

    class Meta:
        managed = False
        db_table = 'quizzes'

class Artefact(models.Model):
    artefactId = models.AutoField(db_column='artefactId', primary_key=True)  
    info = models.CharField(db_column='info', blank=True, null=False)  
    artefactDate = models.DateField(db_column='artefactDate', blank=True, null=False)  
    artefactObjectPath = models.TextField(db_column='artefactObjectPath', blank=True, null=False)  
    exhibitId = models.ForeignKey(Exhibit, models.CASCADE, db_column='exhibitId')  

class Users(models.Model):
    userId = models.AutoField(db_column='userId', primary_key=True, blank=True, null=False)   
    userLevel = models.IntegerField(db_column='userLevel')   
    fName = models.CharField(db_column='fName', blank=True, null=False)   
    lName = models.CharField(db_column='lName', blank=True, null=False)  
    password = models.CharField(db_column='password', blank=True, null=False)  
    totalQuizzPoints = models.IntegerField(db_column='totalQuizzPoints', blank=True, null=False) 

    class Meta:
        managed = False
        db_table = 'users'

class AiSystemDescription(models.Model):
    systemDescriptionId = models.AutoField(db_column='systemDescriptionId', primary_key=True, null=False)   
    exhibit = models.OneToOneField(Exhibit, on_delete=models.CASCADE,related_name='systemDescription', blank= True, null = True)
    systemDescription = models.TextField(db_column='systemDescription', blank=True, null=False)   
    systemPurpose = models.TextField(db_column='systemPurpose', blank=True, null=False)   
    systemOutputs = models.TextField(db_column='systemOutputs', blank=True, null=False)   

    class Meta:
        managed = True
        db_table = 'AI_system_description'





class AttemptedQuizzes(models.Model):
    pk = models.CompositePrimaryKey('userId', 'quizId')
    userId = models.ForeignKey(Users, models.CASCADE, db_column='userId', blank=True, null=False)   
    quizId = models.ForeignKey(Quizzes, models.CASCADE, db_column='quizId', blank=True, null=False)   
    pointsGained = models.IntegerField(db_column='pointsGained', blank=True, null=False)   
    attemptDate = models.DateField(db_column='attemptDate', blank=True, null=False)   

    class Meta:
        managed = False
        db_table = 'attempted_quizzes'





class BookMarks(models.Model):
    pk = models.CompositePrimaryKey('userId', 'exhibitId')
    userId = models.ForeignKey(Users, models.CASCADE, db_column='userId', blank=True, null=False)   
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







class QuizzQuestions(models.Model):
    questionId = models.AutoField(db_column='questionId', primary_key=True, blank=True, null=False)   
    quizId = models.ForeignKey(Quizzes, models.CASCADE, db_column='quizId', blank=True, null=False)   
    question = models.TextField(db_column='question', null=False)
    option1 =  models.TextField(db_column='option1', null=False)  
    option2 = models.TextField(db_column='option2', null=False)
    option3 = models.TextField(db_column='option3', null=False)
    option4 = models.TextField(db_column='option4', null=False)
    questionAnswer = models.IntegerField(db_column='questionAnswer')   
    completionRate = models.IntegerField(db_column='completionRate', blank=True, null=False)   
    attemptRate = models.IntegerField(db_column='attemptRate', blank=True, null=False)   
    points = models.IntegerField(db_column='points', blank=True, null=False)   

    class Meta:
        managed = False
        db_table = 'quizz_questions'
        


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