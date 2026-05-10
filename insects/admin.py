from django.contrib import admin
from .models import ContentOrder, ContentFamily, ContentSpecies

admin.site.register(ContentOrder)
admin.site.register(ContentFamily)
admin.site.register(ContentSpecies)