from django.contrib import admin

# Register your models here.

from .models import Task


class NewAdmin(admin.ModelAdmin):

    list_display = ("title", "task",)


admin.site.register(Task, NewAdmin)
