from django.db import models
from auths.models import CustomUser

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=124, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Вопрос')

    class Meta:
        ordering = ('id',)
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self) -> str:
        return self.title

class Answer(models.Model):
    qusetion_id = models.ForeignKey(Question, verbose_name=("Вопрос"), related_name='answers', on_delete=models.SET_NULL, null=True)
    text = models.CharField(max_length=254, verbose_name='Ответ')
    is_right = models.BooleanField(verbose_name='Правильный ли ответ')

    class Meta:
        ordering = ('id',)
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

    def __str__(self) -> str:
        return self.text

class UserAnswer(models.Model):
    user_id = models.ForeignKey(CustomUser, verbose_name=("Пользователь"), on_delete=models.SET_NULL, null=True)
    right_answer_id = models.ForeignKey(Answer, verbose_name="Ответ", on_delete=models.SET_NULL, null=True)
    question_id = models.ForeignKey(Question, verbose_name=("Вопрос"), on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Ответ пользователя'
        verbose_name_plural = 'Ответы пользователей'
    
    def __str__(self) -> str:
        return str(self.user_id)
