from django.db import models
from django.contrib import admin
from django.utils.html import format_html,mark_safe

from io import BytesIO
from base64 import b64encode

# Create your models here.

class CaptchaAnwser(models.Model):
    site = models.CharField(max_length=30)
    img_content = models.BinaryField()
    anwser = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now=True)

    def img_content_thumb(self):
        if self.img_content:
            file_like = b64encode(self.img_content)

            return mark_safe(u'<img width=200 src="data:image/png;base64,%s" />') % file_like.decode('utf-8')
        else:
            return '(No image)'

    img_content_thumb.short_description = 'Captcha Image'
    img_content_thumb.allow_tags = True






