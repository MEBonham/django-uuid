from django.shortcuts import render
from django.http import HttpResponse
import time
import uuid


def index(request):
    return HttpResponse("Hello, world. " + time.strftime("%c") + "<br/>" +
                        "You are now known by the number " + str(uuid.uuid1()))