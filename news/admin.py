from django.contrib import admin
from .models import News, HeaderModel

# Register your models here.

admin.site.register(News)
admin.site.register(HeaderModel)


admin.site.site_header = "News"
