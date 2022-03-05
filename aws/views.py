from django.views.generic import View
from aws.models import Matter
from django.views.generic.list import ListView


class MatterList(ListView):
    model = Matter
