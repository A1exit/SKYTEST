from django.urls import path
from resume.views import ChangeResumeView, GetResumeListView

urlpatterns = [
    path("<int:pk>/", ChangeResumeView.as_view(), name="update_resume"),
    path("", GetResumeListView.as_view(), name="resume_list"),
]
