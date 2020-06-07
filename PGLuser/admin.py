from django.contrib import admin
from .models import Pgluser

# Register your models here.


class PgluserAdmin(admin.ModelAdmin):
    list_display = ('email', 'password')


admin.site.register(Pgluser, PgluserAdmin)
