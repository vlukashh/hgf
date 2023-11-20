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

class Category(models.Model):
    name = models.CharField(verbose_name="Категория", max_length=150, blank=False)

    def __str__(self):
        return self.name



class Appli(models.Model):
    name = models.CharField(verbose_name="Название", max_length=150, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    desc = models.CharField(verbose_name="Описание", max_length=150, blank=False)
    cat = models.ForeignKey("Category", verbose_name="Категория", max_length=150, blank=False, on_delete=models.CASCADE)
    image_app = models.ImageField(verbose_name="Фотография", upload_to='images/', blank=False, validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg', 'bmp'])])
    user = models.ForeignKey(AdvUser, on_delete=models.CASCADE, verbose_name="Пользователь")

    STATUS_CHOICES = (
        ('Н', 'Новая'),
        ('П', 'Принята в работу'),
        ('В', 'Выполнено'),
    )

    stas = models.CharField(verbose_name="Статус заявки", max_length=1, choices=STATUS_CHOICES, blank=False,
                                  default='Н')

    image_admin = models.ImageField(verbose_name="Фотография дизайна", upload_to='images_admin/', validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg', 'bmp'])],
                                    help_text="Указать фото дизайна при смене статуса на 'Выполнено'", blank=True)

    comment_admin = models.TextField(verbose_name="Комментарий", help_text="Указать комментарий при смене статуса на 'Принята в работу'", blank=True)

    def __str__(self):
        return f"{self.name}, {self.cat}"
