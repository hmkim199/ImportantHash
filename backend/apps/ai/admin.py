from django.contrib import admin

from .models import Importance, Keyword, Frequency

admin.site.register(Importance)
admin.site.register(Keyword)
admin.site.register(Frequency)