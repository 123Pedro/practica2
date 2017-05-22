from django.http import HttpResponse

def index(request):
    return HttpResponse( '<h1>Lista de musica</h1>');