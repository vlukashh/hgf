from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator, FileExtensionValidator



class AdvUser(AbstractUser):

    login_validator = RegexValidator(
        regex=r"^[a-zA-Z-]+$",
        message="Введите допустимое слово. Должно содержать латиницу и дефисы."
    )

    fio_validator = RegexValidator(
        regex=r"^[а-яА-Я-]+\s[а-яА-Я-]+\s[а-яА-Я-]+$",
        message="Введите допустимое слово. Должно содержать кириллицу, пробелы и дефисы"
    )

    username = models.CharField(
        verbose_name="Логин",
        max_length=150,
        unique=True,
        blank=False,
        help_text=(
            "Разрешается использовать только латиницу и дефис."
        ),
        validators=[login_validator],
        error_messages={
            "unique": "Пользователь с таким именем уже существует.",
        },
    )
    first_name = models.CharField(verbose_name="ФИО", max_length=150, blank=False, validators=[fio_validator], help_text=(
            "Разрешается использовать только кириллицу, пробелы и дефис."))
    email = models.EmailField(verbose_name="Почта", blank=False)

