from django.shortcuts import render, redirect, HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .models import School, Subject
from .forms import SchoolForm, SubjectForm

# Create your views here.
class HomeView(TemplateView):
    template_name = "python/home.html"


class SchoolCreate(CreateView):
    model = School
    form_class = SchoolForm
    template_name = "python/create.html"

class SchoolView(ListView):
    model = School
    template_name = "python/list.html"

class SubjectCreate(CreateView):
    model = Subject
    form_class = SubjectForm
    template_name = "python/create.html"

class SubjectView(ListView):
    model = Subject
    template_name = "python/subjectlist.html"