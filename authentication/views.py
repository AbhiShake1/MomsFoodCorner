from django.http import HttpRequest, HttpResponse, JsonResponse


# Create your views here.
def signup(request: HttpRequest) -> JsonResponse:
    username = request.POST.get('username')
    password = request.POST.get('password')
    return JsonResponse({
        'username': username,
        'password': password,
    })
