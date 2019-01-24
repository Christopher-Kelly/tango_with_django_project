from django.contrib import admin
from django.contrib import admin.ModelAdmin
from rango.models import Category, Page

admin.site.register(Category)
admin.site.register(Page,PageAdmin)

class PageAdmin(admin.ModelAdmin):
    list_display = {'title','category','admin'}
# Register your models here.
