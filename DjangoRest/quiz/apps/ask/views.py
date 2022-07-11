from rest_framework import viewsets

from ask.models import Question
from ask.serializers import QuestionSerializer

# Create your views here.
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

