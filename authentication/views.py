from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse, JsonResponse

from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def signup(request: HttpRequest) -> JsonResponse:
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        try:
            user: User = User.objects.create_user(username, username, password,
                                                  first_name=first_name, last_name=last_name
                                                  )
            return JsonResponse({
                'username': user.username,
                'dateJoined': user.date_joined,
                'isAdmin': user.is_superuser,
            })
        except Exception as e:
            return JsonResponse({'Error': str(e)}, status=401)
    return JsonResponse({'Error': 'Only POST Allowed'}, status=403)


def get_user(_, username: str) -> JsonResponse:
    user: User = User.objects.get_by_natural_key(username=username)
    if user:
        return JsonResponse({
            'username': user.username,
            'dateJoined': user.date_joined,
            'isAdmin': user.is_superuser,
        })
    return JsonResponse({'Error': 'No such user'})


@csrf_exempt
def login_user(request: HttpRequest) -> JsonResponse:
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return JsonResponse({
                    'username': user.username,
                    'dateJoined': user.date_joined,
                    'isAdmin': user.is_superuser,
                })
            return JsonResponse({'Error': 'Invalid Credentials'}, status=401)
        except Exception as e:
            return JsonResponse({'Error': str(e)}, status=401)
    return JsonResponse({'Error': 'Only POST Allowed'}, status=403)
