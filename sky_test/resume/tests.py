from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from rest_framework_simplejwt.tokens import AccessToken

from resume.models import Resume, Grade, Status
from resume.serializers import ResumeSerializer


class ResumeTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = User.objects.create(username="user", password="password")

        Resume.objects.create(
            experience="testexperience",
            portfolio="https://github.com/",
            title="testitle",
            phone="+79650118110",
            email="testemail@test.com",
            user=self.user,
            status=Status.not_published,
            grade=Grade.intern,
        )
        Resume.objects.create(
            experience="testexperience2",
            portfolio="https://github.com/",
            title="testitle2",
            phone="+79650118110",
            email="testemail2@test.com",
            user=self.user,
            status=Status.not_published,
            grade=Grade.intern,
        )
        Resume.objects.create(
            experience="testexperience3",
            portfolio="https://github.com/",
            title="testitle3",
            phone="+79650118110",
            email="testemail3@test.com",
            user=self.user,
            status=Status.not_published,
            grade=Grade.intern,
        )

    def test_get_user_resumes(self):
        response = self.client.get("/resume/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_resumes_no_authentication(self):
        response = self.client.patch("/resume/2/", data={"title": "new_title"})

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(
            response.data,
            {"detail": "Authentication credentials were not provided."},
        )

    def test_update_user_resume(self):
        access_token = AccessToken.for_user(self.user)
        self.client.force_authenticate(user=self.user, token=access_token)

        resume_id = Resume.objects.filter(user=self.user).first().id
        response = self.client.patch(
            f"/resume/{resume_id}/",
            data={"title": "new_title", "phone": "+79650118111"},
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        resume = Resume.objects.get(id=resume_id)
        serializer = ResumeSerializer(resume)
        self.assertEqual(response.data, serializer.data)

    def test_put_method_not_allowed(self):
        access_token = AccessToken.for_user(self.user)
        self.client.force_authenticate(user=self.user, token=access_token)
        response = self.client.put(
            "/resume/1/", data={"title": "new_title", "phone": "+88005553535"}
        )

        self.assertEqual(
            response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED
        )
        self.assertEqual(
            response.data,
            {"detail": "Method Not Allowed"},
        )
