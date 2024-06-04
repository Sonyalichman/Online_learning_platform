from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Material, Project, Comment
from .forms import MaterialForm, ProjectForm, CommentForm, SearchForm

@login_required
def materials_list(request):
    form = SearchForm(request.GET)
    query = request.GET.get('query')
    if query:
        materials = Material.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
    else:
        materials = Material.objects.all()
    return render(request, 'materials/materials_list.html', {'materials': materials, 'form': form, 'query': query})

@login_required
def upload_material(request):
    if request.method == 'POST':
        form = MaterialForm(request.POST, request.FILES)
        if form.is_valid():
            material = form.save(commit=False)
            material.uploaded_by = request.user
            material.save()
            return redirect('materials_list')
    else:
        form = MaterialForm()
    return render(request, 'materials/upload_material.html', {'form': form})

@login_required
def projects_list(request):
    form = SearchForm(request.GET)
    query = request.GET.get('query')
    if query:
        projects = Project.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
    else:
        projects = Project.objects.all()
    return render(request, 'materials/projects_list.html', {'projects': projects, 'form': form})

@login_required
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.save()
            form.save_m2m()  # Save ManyToMany relationships
            return redirect('projects_list')
    else:
        form = ProjectForm()
    return render(request, 'materials/create_project.html', {'form': form})

@login_required
def add_comment_to_material(request, pk):
    material = get_object_or_404(Material, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.material = material
            comment.author = request.user
            comment.save()
            return redirect('materials_list')
    else:
        form = CommentForm()
    return render(request, 'materials/add_comment_to_material.html', {'form': form})

@login_required
def project_details(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'materials/project_details.html', {'project': project})

@login_required
def add_comment_to_material(request, pk):
    material = get_object_or_404(Material, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.material = material
            comment.author = request.user
            comment.save()
            return redirect('materials_list')
    else:
        form = CommentForm()
    return render(request, 'materials/add_comment_to_material.html', {'form': form})

@login_required
def add_comment_to_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.project = project
            comment.author = request.user
            comment.save()
            return redirect('project_details', pk=project.pk)
    else:
        form = CommentForm()
    return render(request, 'materials/add_comment_to_project.html', {'form': form, 'project': project})

