from django.contrib import admin
from ask.models import Question, Answer, UserAnswer

# Register your models here.
admin.site.register([Question, Answer, UserAnswer])