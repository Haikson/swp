from django.db import models
from django.contrib.auth.models import User


class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_at', '-pk')

    def popular(self):
        return self.order_by('-likes')

class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, null=True, blank=True)
    likes = models.ManyToManyField(User, related_name='question_like_user')

    objects = QuestionManager()

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-added_at', 'title']
        verbose_name = "Question"
        verbose_name_plural = "Questions"


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)
    question = models.ForeignKey('Question')
    author = models.ForeignKey(User, null=True, blank=True)

    class Meta:
        verbose_name = "Answer"
        verbose_name_plural = "Answers"

    def __unicode__(self):
        pass
    

