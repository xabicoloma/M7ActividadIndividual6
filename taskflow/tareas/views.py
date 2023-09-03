from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import Post
from .forms import PostForm
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
def index(request):
    return render (request, 'tareas/index.html')

def home(request):
    return render (request, 'tareas/home.html')

@method_decorator(login_required, name='dispatch')
class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'tareas/home.html'
    context_object_name = 'context'

    def get_queryset(self):
        # Filter the queryset to only include tasks created by the currently logged-in user
        queryset = Post.objects.filter(author=self.request.user)

        etiqueta_tarea = self.request.GET.get('etiqueta_tarea')
        if etiqueta_tarea:
            queryset = queryset.filter(etiqueta_tarea=etiqueta_tarea)
        
        queryset = queryset.exclude(tzone='Completada')
        
        return queryset
    
@method_decorator(login_required, name='dispatch')
class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'tareas/crear_posteo.html'
    success_url = reverse_lazy('home')

@method_decorator(login_required, name='dispatch')
class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'tareas/modificar_posteo.html'
    success_url = reverse_lazy('home')

@method_decorator(login_required, name='dispatch')
class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('home')

@login_required
def cambiar_status(request, id):
    post = Post.objects.get(pk=id)
    if request.method == 'POST':
        post.tzone = 'Completada'
        post.save()
        return redirect('home')
    
@login_required
def new_status(request, id):
    post = Post.objects.get(pk=id)
    if request.method == 'POST':
        new_status = request.POST.get('new_status', '')
        post.observations = new_status
        post.save()
        return redirect('home')

@login_required
def main_task_list(request, CreateView):
    tasks = Post.objects.exclude(tzone='Completada')
    return render(request, 'home', {'tasks': tasks})

@login_required
def completed_task_list(request):
    completed_tasks = Post.objects.filter(tzone='Completada')
    return render(request, 'tareas/tareas_completadas.html', {'completed_tasks': completed_tasks})