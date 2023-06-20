from django.contrib import admin
from resume.models import Resume


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "email",
        "phone",
        "portfolio",
        "grade",
    )
    list_filter = (
        "title",
        "status",
    )
    search_fields = (
        "title",
        "email",
        "phone",
    )
