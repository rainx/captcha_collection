from django.contrib import admin

from .models import CaptchaAnwser
# Register your models here.

class CaptchaAnwserAdmin(admin.ModelAdmin):
    list_display = ('site', 'img_content_thumb', 'anwser')

admin.site.register(CaptchaAnwser, CaptchaAnwserAdmin)