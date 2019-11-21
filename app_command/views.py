from .models import SaveBirth
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import datetime


@csrf_exempt
def save_birth(request):
    user_name = request.POST.get("user_name", None)
    birthdate = request.POST.get("text", None)

    birth_day = datetime.datetime.strptime(birthdate, "%Y/%M/%d").date()

    SaveBirth.objects.create(
        name=user_name,
        birth_day=birth_day,
    )

    return JsonResponse({
        'text': f'{user_name} {birth_day} created',
    })
