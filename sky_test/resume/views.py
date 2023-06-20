from django.db.models import QuerySet
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import ListAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from resume.models import Resume
from resume.serializers import ResumeSerializer


class GetResumeListView(ListAPIView):
    permission_classes = (AllowAny,)
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    allowed_methods = ("GET",)

    def get(self, request) -> Response:
        """Возвращает курсы и книги по поиску

        request:
            - request: request - запрос пользователя
        returns:
            - status: status.HTTP_200_OK - статус успешной обработки запроса
            - data: json - данные по резюме
        """

        resume = self.get_queryset()
        resume_data = ResumeSerializer(resume, many=True)
        return Response(
            status=status.HTTP_200_OK,
            data=resume_data.data,
        )


class ChangeResumeView(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ResumeSerializer
    allowed_methods = ("PATCH",)

    def patch(self, request, pk: int) -> Response:
        """Изменяет данные в резюме.

        request:
            - request: request - запрос пользователя
            - pk: id резюме, которое необходимо изменить
            - data: json - данные по резюме
        returns:
            - status: status.HTTP_200_OK - статус успешной обработки запроса
            - data: json - данные по резюме
        """
        resume = self.get_queryset(pk)
        if resume.user_id == request.user.id:
            serializer = ResumeSerializer(
                resume, data=request.data, partial=True
            )
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(
                    serializer.errors, status=status.HTTP_400_BAD_REQUEST
                )
        return Response(
            {"detail": "Вы можете редактировать только свое резюме"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    def put(self, request, pk: int) -> Response:
        return Response(
            {"detail": "Method Not Allowed"},
            status=status.HTTP_405_METHOD_NOT_ALLOWED,
        )

    def get_queryset(self, pk: int) -> QuerySet:
        return get_object_or_404(Resume, id=pk)
