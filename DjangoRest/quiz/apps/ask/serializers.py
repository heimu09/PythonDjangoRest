from rest_framework import serializers

from ask.models import Question, Answer


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = '__all__'
    
    def create(self, validated_data):
        answers_data = validated_data.pop('answers')
        qusetion = Question.objects.create(**validated_data)
        
        for track_data in answers_data:
            Answer.objects.create(qusetion_id=qusetion, **track_data)

        return qusetion