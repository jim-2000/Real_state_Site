from django.contrib import admin
from .models import ConstractionCatagory, ConstractionProject
# Register your models here.

class AdminConstructorCatagory(admin.ModelAdmin):
    list_display = ['title', 'status','create_at', 'update_at']
    list_filter = ['status', 'create_at']
    prepopulated_fields = {'slug':('title',)}

admin.site.register(ConstractionCatagory, AdminConstructorCatagory)


class AdminConstructorProject(admin.ModelAdmin):
    list_display = ['title','image_tag' ,'create_at','status', 'update_at']
    list_filter = ['status', 'create_at']
    prepopulated_fields = {'slug':('title',)}

admin.site.register(ConstractionProject,AdminConstructorProject)