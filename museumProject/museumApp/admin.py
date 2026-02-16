from django.contrib import admin
from .models import *


admin.site.site_header = "Museum Admin"
admin.site.index_title = "Museum Admin Portal"

admin.site.register(Exhibit)
admin.site.register(Artefact)
admin.site.register(AiSystemDescription)
admin.site.register(ContributingFactors)
admin.site.register(FailureDescription)
admin.site.register(LessonsLearned)


