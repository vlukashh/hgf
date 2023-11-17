from django.contrib import admin
from .models import Category
from .models import AdvUser
from .models import Appli


admin.site.register(AdvUser)

admin.site.register(Category)

admin.site.register(Appli)
