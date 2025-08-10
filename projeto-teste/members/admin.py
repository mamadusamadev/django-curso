from django.contrib import admin
from .models import Members

# Register your models here.

#admin.site.register(Members)


class MemberAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "phone", "data_joined")

admin.site.register(Members, MemberAdmin)