from django.http import HttpResponse


def index(request):
    return HttpResponse("Hola , me encuentro en la aplicacion de Home.")