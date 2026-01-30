from django.db import models

class Exhibit(models.Model):
    exhibitid = models.AutoField(db_column='ExhibitId', primary_key=True)  
    title = models.TextField(db_column='Title', blank=True, null=True) 
    domain = models.TextField(db_column='Domain', blank=True, null=True)  
    backgrounddeploymentcontext = models.TextField(db_column='BackgroundDeploymentContext', blank=True, null=True) 
    intededuse = models.TextField(db_column='IntededUse', blank=True, null=True) 
    viewnumber = models.IntegerField(db_column='ViewNumber', blank=True, null=True)  

class Artefact(models.Model):
    artefactid = models.AutoField(db_column='ArtefactId', primary_key=True)  
    info = models.CharField(db_column='Info', blank=True, null=True)  
    artefactdate = models.DateField(db_column='ArtefactDate', blank=True, null=True)  
    artefactobjectpath = models.TextField(db_column='ArtefactObjectPath', blank=True, null=True)  
    exhibitid = models.ForeignKey(Exhibit, models.CASCADE, db_column='ExhibitId')  


"""
class AiSystemDescription(models.Model):
    systemdescriptionid = models.AutoField(db_column='SystemDescriptionId', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    exhibitid = models.ForeignKey('Exhibit', models.DO_NOTHING, db_column='ExhibitId', blank=True, null=True)  # Field name made lowercase.
    systemdescription = models.TextField(db_column='SystemDescription', blank=True, null=True)  # Field name made lowercase.
    systempurpose = models.TextField(db_column='SystemPurpose', blank=True, null=True)  # Field name made lowercase.
    systemoutputs = models.TextField(db_column='SystemOutputs', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AI_system_description'





class AttemptedQuizzes(models.Model):
    pk = models.CompositePrimaryKey('UserId', 'QuizId')
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='UserId', blank=True, null=True)  # Field name made lowercase.
    quizid = models.ForeignKey('Quizzes', models.DO_NOTHING, db_column='QuizId', blank=True, null=True)  # Field name made lowercase.
    pointsgained = models.IntegerField(db_column='PointsGained', blank=True, null=True)  # Field name made lowercase.
    attemptdate = models.DateField(db_column='AttemptDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'attempted_quizzes'


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


class BookMarks(models.Model):
    userid = models.OneToOneField('Users', models.DO_NOTHING, db_column='UserId', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    exhibitid = models.ForeignKey('Exhibit', models.DO_NOTHING, db_column='ExhibitId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'book_marks'


class ContributingFactors(models.Model):
    contributingfactorid = models.AutoField(db_column='ContributingFactorId', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    exhibitid = models.ForeignKey('Exhibit', models.DO_NOTHING, db_column='ExhibitId', blank=True, null=True)  # Field name made lowercase.
    dataissues = models.TextField(db_column='DataIssues', blank=True, null=True)  # Field name made lowercase.
    designchoices = models.TextField(db_column='DesignChoices', blank=True, null=True)  # Field name made lowercase.
    organisationalorgovernanceissues = models.TextField(db_column='OrganisationalOrGovernanceIssues', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'contributing_factors'


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








class FailureDescription(models.Model):
    failuredescriptionid = models.AutoField(db_column='FailureDescriptionId', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    exhibitid = models.ForeignKey(Exhibit, models.DO_NOTHING, db_column='ExhibitId', blank=True, null=True)  # Field name made lowercase.
    whatwentwrong = models.TextField(db_column='WhatWentWrong', blank=True, null=True)  # Field name made lowercase.
    howitwasdetected = models.TextField(db_column='HowItWasDetected', blank=True, null=True)  # Field name made lowercase.
    whatwasaffected = models.TextField(db_column='WhatWasAffected', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'failure_description'


class LessonsLearned(models.Model):
    lessonslearnedid = models.AutoField(db_column='LessonsLearnedId', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    exhibitid = models.ForeignKey(Exhibit, models.DO_NOTHING, db_column='ExhibitId', blank=True, null=True)  # Field name made lowercase.
    practicalrecommendations = models.TextField(db_column='PracticalRecommendations', blank=True, null=True)  # Field name made lowercase.
    futurewarnings = models.TextField(db_column='FutureWarnings', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lessons_learned'


class QuizzQuestions(models.Model):
    questionid = models.AutoField(db_column='QuestionId', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    quizid = models.ForeignKey('Quizzes', models.DO_NOTHING, db_column='QuizId', blank=True, null=True)  # Field name made lowercase.
    question = models.TextField(db_column='Question', blank=True, null=True)  # Field name made lowercase.
    questionanswer = models.TextField(db_column='QuestionAnswer', blank=True, null=True)  # Field name made lowercase.
    completionrate = models.IntegerField(db_column='CompletionRate', blank=True, null=True)  # Field name made lowercase.
    attemptrate = models.IntegerField(db_column='AttemptRate', blank=True, null=True)  # Field name made lowercase.
    points = models.IntegerField(db_column='Points', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'quizz_questions'


class Quizzes(models.Model):
    quizid = models.AutoField(db_column='QuizId', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    exhibitid = models.ForeignKey(Exhibit, models.DO_NOTHING, db_column='ExhibitId', blank=True, null=True)  # Field name made lowercase.
    quizzdetails = models.TextField(db_column='QuizzDetails', blank=True, null=True)  # Field name made lowercase.
    completionrate = models.IntegerField(db_column='CompletionRate', blank=True, null=True)  # Field name made lowercase.
    attemptrate = models.IntegerField(db_column='AttemptRate', blank=True, null=True)  # Field name made lowercase.
    totalquestionpoints = models.IntegerField(db_column='TotalQuestionPoints', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'quizzes'


class Users(models.Model):
    userid = models.AutoField(db_column='UserId', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    user_level = models.IntegerField(db_column='User_Level')  # Field name made lowercase.
    fname = models.CharField(db_column='FName', blank=True, null=True)  # Field name made lowercase.
    lname = models.CharField(db_column='LName', blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', blank=True, null=True)  # Field name made lowercase.
    totalquizzpoints = models.IntegerField(db_column='TotalQuizzPoints', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'users'

"""