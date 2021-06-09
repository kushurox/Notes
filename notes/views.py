from django.http import HttpResponse

def main_home(req):
    return HttpResponse('Default Page 200')