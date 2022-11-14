from django.contrib import admin
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'status')
    list_filter = ("status",)
    list_image = ("image",)
    search_fields = ['title', 'content']

admin.site.register(Project, ProjectAdmin)