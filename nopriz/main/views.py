from django.template import loader
from django.http import HttpResponse

from . import models


def index(request):
    template = loader.get_template('main/index.html')
    user = None
    if request.GET:
        code = request.GET['s.registrationNumber']
        user = models.User.objects.get(code=code)
    return HttpResponse(template.render({'user': user}, request))

def qr(request):
    template = loader.get_template('main/qr.html')
    user = None
    if request.GET:
        code = request.GET['s.registrationNumber']
        user = models.User.objects.get(code=code)
    return HttpResponse(template.render({'user': user}, request))