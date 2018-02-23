from django.contrib import admin

# Register your models here.
from django.contrib import admin
from learnlogs.models import Topic,Entry
admin.site.register(Topic)
admin.site.register(Entry)