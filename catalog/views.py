from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1>RentalOps</h1><p>Coming soon</p>")
