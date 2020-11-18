from django.contrib import admin
from .models import Person, GroupPerson


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass


@admin.register(GroupPerson)
class GroupPersonAdmin(admin.ModelAdmin):
    pass
