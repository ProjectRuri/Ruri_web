from django.shortcuts import render

from django.http import HttpResponse

import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from pyClient import test

def index(request):
    test.printValue("test")
    return render(request, 'ruri/main.html')
    # return HttpResponse("안녕하세요 pybo에 오신것을 환영합니다.")
