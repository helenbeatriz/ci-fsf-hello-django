from django.shortcuts import render


# Create your views here.
def get_todo_list(request):
    return render(request, 'todo/todo_list.html')
def say_hello(request):
    return HttpResponse("Hello!")

