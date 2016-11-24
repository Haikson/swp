from django import forms
from models import Question, Answer
from django.contrib.auth.models import User


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


class SignupForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        data = self.cleaned_data
        username = data['username']
        try:
            user = User.objects.get(username=username)
            raise forms.ValidationError('User %s exist' % username)
        except User.DoesNotExist:
            pass
        return data

    def save(self):
        data = self.cleaned_data
        username = data['username']
        email = data['email']
        password = data['password']

        user = User.objects.create_user(username, email, password)
        user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        data = self.cleaned_data
        return data

