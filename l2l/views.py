from datetime import datetime
from .constants import DATE_FORMAT
from django.http import HttpResponse
from django.template import loader


def index(request):
    now = datetime.now()
    template = loader.get_template('l2l/index.html')
    context = {
        'iso': now.strftime(DATE_FORMAT),
        'now': now,
    }
    return HttpResponse(template.render(context, request))
