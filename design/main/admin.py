from django.contrib import admin
from .models import Category
from .models import AdvUser
from .models import Appli
from .forms import CheckAppliForm


@admin.register(AdvUser)
class AdvUserAdmin(admin.ModelAdmin):
    list_display = ("username", "email")


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Appli)
class AdminAppli(admin.ModelAdmin):
    form = CheckAppliForm
    list_display = ("name", "cat")