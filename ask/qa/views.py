from django.http import Http404
from django.shortcuts import render
from .models import Question

# Create your views here.
from django.http import HttpResponse 

def test(request, *args, **kwargs):
    return HttpResponse('Dummy view.')

def main_page(request, *args, **kwargs):
    return HttpResponse('Main page.')

def popular_page(request, *args, **kwargs):
    return HttpResponse('Popular question page.')

def question_id_page(request, question_id):
    try:
        question = Question.objects.get(id=question_id)
    except Question.DoesNotExist:
        raise Http404

    return render(request, 'question_post.html', {
        'title': question.title,
        'text': question.text,
    })
