from django.contrib import admin
from .models import App
# Register your models here.

#I have created this because need to check the data in admin portal and confirm celerytaskworked perfectly or not 
@admin.register(App)
class UserAdmin(admin.ModelAdmin):
    list_display = ('title', 'summary', 'contentRating', 'genre', 'installs', 'url')