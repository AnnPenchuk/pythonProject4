from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView
from .forms import TaskForm
from .models import Task


def index(request):
    news = Task.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': news})


def about(request):
    return render(request, 'main/about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма введена неправильно'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)


class Home(TemplateView):

   template_name = 'base.html'


class Search(ListView):
    model = Task

    template_name = 'search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')

        object_list = Task.objects.filter(title=query)

        return object_list

