from rest_framework import serializers
from resume.models import Resume


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = (
            "title",
            "phone",
            "email",
            "portfolio",
            "grade",
            "salary",
            "education",
            "experience",
            "specialty",
            "status",
        )
