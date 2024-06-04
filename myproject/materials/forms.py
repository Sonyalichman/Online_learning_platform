from django import forms
from .models import Material, Project, Comment

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['title', 'description', 'file']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'participants']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)
