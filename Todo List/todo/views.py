
from django.shortcuts import render, redirect,HttpResponse
from django.views.decorators.http import require_POST

from .models import Contact, Review, todo
from .forms import todoForm

def home(request):
    todo_list = todo.objects.order_by('id')

    form = todoForm()

    context = {'todo_list' : todo_list, 'form' : form}

    return render(request, 'home.html', context)

def index(request):
    todo_list = todo.objects.order_by('id')

    form = todoForm()

    context = {'todo_list' : todo_list, 'form' : form}

    return render(request, 'index.html', context)
def review(request):
    todo_list = todo.objects.order_by('id')

    form = todoForm()

    context = {'todo_list' : todo_list, 'form' : form}

    return render(request, 'review.html', context)
def contact(request):
    todo_list = todo.objects.order_by('id')

    form = todoForm()

    context = {'todo_list' : todo_list, 'form' : form}

    return render(request, 'contact.html', context)
@require_POST
def addTodo(request):
    form = todoForm(request.POST)

    if form.is_valid():
        new_todo = todo(text=request.POST['text'])
        new_todo.save()





    return redirect('index')

def addReview(request):
    if request.method == 'POST':
        name = request.POST['Name']
        review = request.POST['Feedback']
        new_review=Review(name = name, review = review)
        new_review.save()
    return HttpResponse('Review Added Succesfully')

def addContact(request):
    if request.method == 'POST':
        email = request.POST['Email']
        query = request.POST['Query']
        new_query=Contact(email = email, query = query)
        new_query.save()
    return HttpResponse('Your Query will be rectified soon')

def completeTodo(request, todo_id):
    todo = todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()

    return redirect('index')

def deleteCompleted(request):
    todo.objects.filter(complete__exact=True).delete()

    return redirect('index')

def deleteAll(request):
    todo.objects.all().delete()

    return redirect('index')