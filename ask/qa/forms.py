from django import forms
from models import Question, Answer


class AskForm(forms.Form):
    title = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        data = self.cleaned_data
        return data

    def save(self, user=None):
        data = self.cleaned_data
        title = data['title']
        text = data['text']

        question = Question(
                title=title,
                text=text,
                author=user
            )

        question.save()
        return question


class AnswerForm(forms.Form):
    question = forms.IntegerField(widget=forms.HiddenInput)
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        data = self.cleaned_data

        return data

    def save(self, user=None):
        data = self.cleaned_data
        question = Question.objects.get(pk=data['question'])
        text = data['text']

        answer = Answer(
                question=question,
                text=text,
                author=user
            )

        answer.save()
        return answer