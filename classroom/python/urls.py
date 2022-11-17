from django.urls import path, include
from python.views import HomeView, SubjectView, SubjectsCreate, SchoolCreate, SubjectsView, SchoolView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('topics/', SubjectView.as_view(), name="topics"),
    # New views below
    path('create/', SchoolCreate.as_view(), name="schoolcreate"),
    path('list/', SchoolView.as_view(), name="schoollist"),
]