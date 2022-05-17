from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse, JsonResponse

from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def signup(request: HttpRequest) -> JsonResponse:
    username = request.POST.get('username')
    password = request.POST.get('password')
    try:
        user: User = User.objects.create_user(username, username, password)
        return JsonResponse({
            'username': user.username,
            'dateJoined': user.date_joined,
            'isAdmin': user.is_superuser,
        })
    except:
        return JsonResponse({'Error': 'Only POST Allowed'}, status=403)


@csrf_exempt
def login(request: HttpRequest) -> JsonResponse:
    username = request.POST.get('username')
    password = request.POST.get('password')
    try:
        user = authenticate(username=username, password=password)
        if user:
            login(username=username, password=password)
            return JsonResponse({
                'username': user.username,
                'dateJoined': user.date_joined,
                'isAdmin': user.is_superuser,
            })
        return JsonResponse({'Error': 'Invalid Credentials'}, status=401)
    except:
        return JsonResponse({'Error': 'Only POST Allowed'}, status=403)
