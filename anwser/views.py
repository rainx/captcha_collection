from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
from .models import CaptchaAnwser
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def post(request: HttpRequest):

    if not ('captcha_file' in request.FILES.keys()):
        return JsonResponse({'success': False})

    img = request.FILES['captcha_file'].file.read()
    anwser = request.POST['anwser']
    site = request.POST['site']

    if (not anwser) or (not site) or (not img):
        return JsonResponse({'success': False})

    captcha = CaptchaAnwser(
        img_content=img,
        anwser=anwser,
        site=site
    )
    captcha.save()
    return JsonResponse({'success': True})