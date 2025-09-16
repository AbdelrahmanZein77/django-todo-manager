from django.shortcuts import render, redirect, get_object_or_404
from .models import Tasks
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .repository import TaskRepository
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from .serializers import TasksSerializer
from rest_framework.response import Response
from rest_framework import status
def sign_up(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            if User.objects.filter(username=username).exists():
                return render(request, 'tasks/sign_up.html', {'error':'the username or password is exist'})

            User.objects.create_user(username=username, password=password)
            return redirect('login')

        return render (request, 'tasks/sign_up.html')
    return render (request, 'tasks/sign_up.html')

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            return render(request, 'tasks/login.html', {'error':'the username and password is not exist'})
        return render(request, 'tasks/login.html')
    return render(request, 'tasks/login.html')

@login_required
def logout_views(request):
    logout(request)
    return redirect('login')


@login_required
def home(request):
    
    if request.method == 'POST':
        title = request.POST.get('title')
        description= request.POST.get('description')

        if title and description:
            Tasks.objects.create(user=request.user, title=title, description=description)
            return redirect('home')

        return render(request, 'tasks/home.html', {'error':'invalid input', 'tasks': request.user.tasks.all()})
    return render(request, 'tasks/home.html', {'tasks': request.user.tasks.all(), 'count':request.user.tasks.count()})

@login_required
def all_tasks(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description= request.POST.get('description')

        if title and description:
            Tasks.objects.create(user=request.user, title=title, description=description)
            return redirect('tasks')

        return render(request, 'tasks/tasks.html', {'error':'invalid input', 'tasks': request.user.tasks.all()})
    return render(request, 'tasks/tasks.html', {'tasks': request.user.tasks.all()})

@login_required
def UpdateTask(request, task_id):
    task = get_object_or_404(Tasks, user=request.user, id=task_id)

    if request.method == 'POST':

        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.complated = 'complated' in request.POST

        if task.title and task.description:
            task.save()
            return redirect('home')
        return render(request, 'tasks/update.html', {'error':'please enter a valid title and description','task':task})

    return render(request, 'tasks/update.html', {'task':task})

@login_required
def Toggle_task(request, task_id):
    task = get_object_or_404(Tasks, user=request.user, id= task_id)
    task.complated = not task.complated
    task.save()
    return redirect('home')

@login_required
def delelte_task(request, task_id):
    task = get_object_or_404(Tasks, user=request.user, id=task_id)
    task.delete()
    return redirect('home')

@api_view(['GET', 'POST'])
def Tasks_api(request):
    if request.method == 'GET':

        tasks = Tasks.objects.filter(user=request.user)
        serializer = TasksSerializer(tasks, many=True)
        return Response(serializer.data)

    if request.method == 'POST':

        title = request.data.get('title')
        description = request.data.get('description')

        if title and description:

            serializer = TasksSerializer(tasks)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error':'title and description are required'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'PUT', 'DELETE'])
def Tasks_api_pk(request, pk):
    task = get_object_or_404(Tasks, pk=pk, user= request.user)

    if request.method == 'GET':
        serializer = TasksSerializer(task)
        return Response(serializer.data)
    
    if request.method == 'PUT':

        serializer = TasksSerializer(task, data=serializer.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error':'title and description are required'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    