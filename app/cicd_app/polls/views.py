from django.http import HttpResponse


def index(request):
    return HttpResponse("Oh hell world")