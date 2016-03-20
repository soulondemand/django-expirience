# -*- coding: utf-8 -*-
from django.http import Http404
from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from .models import Question
from qa.forms import AskForm 
from qa.forms import AnswerForm 
from qa.forms import SignupForm1 

# Create your views here.
from django.http import HttpResponse 

def test(request, *args, **kwargs):
    return HttpResponse('Dummy view.')

def add_ask_page(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        if form.is_valid():
            question = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'add_ask.html', {
        'form': form,
    })

def add_answer(request):
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer_obj = form.save()
            question_obj = answer_obj.question
            url = question_obj.get_url()
            return HttpResponseRedirect(url)


def main_page(request):
    posts = Question.objects.filter()
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, limit)
    paginator.baseurl = '/?page='
    page = paginator.page(page) # Page
    return render(request, 'main_page.html', {
        'posts': page.object_list,
        'paginator': paginator,
        'page': page,
        'title': 'Все вопросы:',
    })

def popular_page(request):
    posts = Question.objects.order_by('-rating')
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, limit)
    paginator.baseurl = '/popular/?page='
    page = paginator.page(page) # Page
    return render(request, 'main_page.html', {
        'posts': page.object_list,
        'paginator': paginator,
        'page': page,
        'title': 'Популярные вопросы:',
    })
   
    return HttpResponse('Popular question page.')

def question_id_page(request, question_id):
    try:
        question = Question.objects.get(id=question_id)
    except Question.DoesNotExist:
        raise Http404
    form = AnswerForm(initial={'question': question_id})
    return render(request, 'question_post.html', {
        'title': question.title,
        'text': question.text,
        'answers': question.answer_set.all()[:],
        'form': form,
    })

def signup_page(request):
    if request.method == "POST":
        form = SignupForm1(request.POST)
        if form.is_valid():
            user = User.objects.create_user( form.cleaned_data["username"],
                    form.cleaned_data["email"],
                    form.cleaned_data["password"]
                    )
            user.save()
            return HttpResponseRedirect("/")
        else:
            return HttpResponseRedirect("/signup/")
    if request.method == "GET":
        form = SignupForm1()
        return render(request, 'signup.html', {
            'title': 'Регистрация нового пользователя',
            'form': form, 
        })


def login_page(request):
    return HttpResponse('Dummy view.')

def logout_page(request):
    logout(request)
    return  HttpResponseRedirect('/')

