from django.http import HttpResponse

# Create your views here.
# HTTP REQUEST <- HTTP RESPONSE


def home(request):  # HTTP REQUEST
    return HttpResponse('Home')  # HTTP RESPONSE


def about(request):
    return HttpResponse('About')


def contact(request):
    return HttpResponse('Contact')
