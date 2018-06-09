from django.contrib import admin

# Register your models here.
from .models import Question, Choice, GeolocationData

admin.site.register(Question)
admin.site.register(GeolocationData)