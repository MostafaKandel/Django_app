from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View,ListView,DetailView,TemplateView,CreateView,UpdateView,DeleteView
from . import models

class IndexView(TemplateView):
    template_name='index.html'

class SchoolListView(ListView):
    model=models.School

class SchoolDetailView(DetailView):
    context_object_name= 'school_detail'
    model=models.School
    template_name='lec/school_detail.html'    

class SchoolCreateView(CreateView):
    fields =('name','principal','location')
    model=models.School    
 
class SchoolUpdateView(UpdateView):
    fields=('name','principal')
    model=models.School

class SchoolDeleteView(DeleteView):
    model=models.School
    success_url=reverse_lazy("lec:list")     
 
    