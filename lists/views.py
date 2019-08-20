from django.http import HttpResponse


def home_page(request):
    return HttpResponse('<html>To-Do</html>')


def header_component():
    pass
