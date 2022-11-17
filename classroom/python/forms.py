from .models import School, Subject
from django import forms

class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = '__all__'

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'