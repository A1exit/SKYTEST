from enum import Enum
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

from django.db import models


class Grade(Enum):
    intern = "интерн"
    junior = "джуниор"
    middle = "миддл"
    senior = "сеньор"
    lead = "лид"


class Status(Enum):
    not_published = "не опубликовано"
    published = "опубликовано"
    blocked = "заблокировано"
    on_moderation = "на модерации"


class Education(Enum):
    secondary = "среднее"
    special_secondary = "среднее специальное"
    unfinished_higher = "неоконченное высшее"
    higher = "высшее"
    bachelor = "бакалавр"
    master = "магистр"
    candidate = "кандидат наук"
    doctor = "доктор наук"


class Speciality(Enum):
    frontend = "фронтенд"
    backend = "бэкенд"
    gamedev = "геймдев"
    devops = "девопс"
    design = "дизайн"
    products = "продукты"
    management = "менеджмент"
    testing = "тестирование"


grade_choices = [(choice.name, choice.value) for choice in Grade]
education_choices = [(choice.name, choice.value) for choice in Education]
status_choices = [(choice.name, choice.value) for choice in Status]
speciality_choices = [(choice.name, choice.value) for choice in Speciality]


class Resume(models.Model):
    title = models.CharField(
        max_length=1000,
        verbose_name="Название резюме",
        help_text="Введите название резюме",
    )
    phone = PhoneNumberField(
        verbose_name="Номер телефона",
        help_text="Введите номер телефона",
        blank=True,
        null=True,
    )
    email = models.EmailField(
        verbose_name="Email",
        help_text="Введите email",
    )
    portfolio = models.URLField(
        verbose_name="Ссылка на портфолио",
        help_text="Введите ссылку на портфолио",
        blank=True,
        null=True,
    )
    grade = models.CharField(
        choices=grade_choices,
        max_length=200,
        verbose_name="Грейд",
        help_text="Выберите грейд",
    )
    salary = models.IntegerField(
        verbose_name="Заработная плата",
        help_text="Выберите заработную плату",
        blank=True,
        null=True,
    )
    education = models.CharField(
        choices=education_choices,
        max_length=200,
        verbose_name="Образование",
        help_text="Выберите образование",
        blank=True,
        null=True,
    )
    experience = models.TextField(
        max_length=200,
        verbose_name="Опыт работы",
        help_text="Расскажите о вашем опыте работы",
        blank=True,
        null=True,
    )
    specialty = models.CharField(
        choices=speciality_choices,
        verbose_name="Специальность",
        help_text="Выберите специальность",
        blank=True,
        null=True,
    )
    status = models.CharField(
        choices=status_choices,
        default=Status.not_published,
        max_length=200,
        verbose_name="Статус",
        help_text="Выберите статус",
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Владелец резюме",
        help_text="Выберите владельца резюме",
    )

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Резюме"
        verbose_name_plural = "Резюме"
