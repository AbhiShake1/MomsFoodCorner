from django.http import HttpRequest, HttpResponse, JsonResponse

from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def signup(request: HttpRequest) -> JsonResponse:
    username = request.POST.get('username')
    password = request.POST.get('password')
    return JsonResponse({
        'username': username,
        'password': password,
    })
