from django.urls import path, include
from python.views import HomeView, SchoolCreate,  SchoolView, SubjectView, SubjectCreate

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    # New views below
    path('create-school/', SchoolCreate.as_view(), name="schoolcreate"),
    path('list-school/', SchoolView.as_view(), name="schoollist"),
    path('create-subject/', SubjectCreate.as_view(), name="subjectcreate"),
    path('list-subject/', SubjectView.as_view(), name="subjectlist"),
]