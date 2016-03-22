# -*- coding: utf-8 -*-
from django.http import Http404
from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from .models import Question
from qa.forms import AskForm, AnswerForm, SignupForm, LoginForm 
import logging
logger = logging.getLogger(__name__)

# Create your views here.
from django.http import HttpResponse 

def test(request, *args, **kwargs):
    return HttpResponse('Dummy view.')

def add_ask_page(request):
    logger.debug("add_ask_page() !")
    if request.method == "POST":
        logger.debug("add_ask_page():  method POST")
        form = AskForm(request.POST)
        logger.debug("add_ask_page():  form created")
        if form.is_valid():
            logger.debug("add_ask_page():  form is valid")
            question = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
        else
            logger.debug("add_ask_page():  form is not valid")
            logger.debug("error: " + form.errors)
            
    else:
        logger.debug("add_ask_page():  metod GET")
        form = AskForm(initial={'author':request.user.id})
    logger.debug("add_ask_page(): return render")
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
    form = AnswerForm(initial={'question': question_id,'author': request.user.id})
    return render(request, 'question_post.html', {
        'title': question.title,
        'text': question.text,
        'answers': question.answer_set.all()[:],
        'form': form,
    })

def signup_page(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user( form.cleaned_data["username"],
                    form.cleaned_data["email"],
                    form.cleaned_data["password"]
                    )
            user.save()
            request.session.flush()
            request.session['signup']=user.username
            return HttpResponseRedirect("/")
        else:
            return HttpResponseRedirect("/signup/")
    if request.method == "GET":
        form = SignupForm()
        return render(request, 'signup.html', {
            'title': 'Регистрация нового пользователя',
            'form': form, 
            'button-text': 'Регистировать',
        })


def login_page(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect("/")
                    # Redirect to a success page.
                #else:
                    # Return a 'disabled account' error message
            #else:
                # Return an 'invalid login' error message.
    if request.method == "GET":
        form = LoginForm()
        return render(request, 'login.html', {
            'title': 'Аутентификация',
            'form': form,
            'button-text': 'Войти',
        })

def logout_page(request):
    logout(request)
    return  HttpResponseRedirect('/')

