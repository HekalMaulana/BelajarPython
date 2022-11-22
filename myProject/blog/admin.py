from django.contrib import admin

from .models import Post

# Register your models here.

class postAdmin (admin.ModelAdmin):
    readonly_fields = ['slug','datePost']

admin.site.register(Post, postAdmin)