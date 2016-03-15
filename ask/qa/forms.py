from django import forms
#from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Question

class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text  = forms.CharField(widget=forms.Textarea)
    def clean_title(self):
        title = self.cleaned_data['title']
        #if not is_ethic(message):
        #    raise forms.ValidationError(
        #        u'Message not valid', code=12)
        return title
    def clean_text(self):
        text = self.cleaned_data['text']
        #if not is_ethic(message):
        #    raise forms.ValidationError(
        #        u'Message not valid', code=12)
        return text
    #def clean(self):
    def save(self):
        user = User.objects.get(id=1)
        question = Question(**self.cleaned_data)
        question.author = user
        question.save()
        return question
    #def __init__(self, question, **kwargs):
    #    self.title = question.title;
    #    self.text = question.text;
    #    self. author= question.author;
    #    super(AskForm, self).__init__(**kwargs)

class AnswerForm(forms.Form):
    text = forms.CharField(max_length=100)
    question = forms.CharField(widget=forms.Textarea)
    def clean_text(self):
        text = self.cleaned_data['text']
        #if not is_ethic(message):
        #    raise forms.ValidationError(
        #        u'Message not valid', code=12)
        return text
    def clean_question(self):
        question = self.cleaned_data['question']
        #if not is_ethic(message):
        #    raise forms.ValidationError(
        #        u'Message not valid', code=12)
        return question
    #def clean():

    #def save(self):
    #    post = Post(**self.cleaned_data)
    #    post.save()
    #    return post    #    return post
