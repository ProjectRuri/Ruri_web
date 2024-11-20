from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import redirect
from .forms import wav_files
from django.views.decorators.csrf import csrf_exempt

import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from pyClient import test
from pyClient import Custom_Encode
def index(request):
    test.printValue("test222")
    # Custom_Encode.c_Encode("testfile.txt"," 테스트")
    return render(request, 'ruri/main.html')
    # return HttpResponse("안녕하세요 pybo에 오신것을 환영합니다.")

@csrf_exempt
def before_wev_file(request):
    return render(request, 'ruri/main.html')


@csrf_exempt
def upload_wav_file(request):
    test.printValue("upload_1 : "+ request.method)

    if request.method == 'POST':
        body = request.body
        test.printValue("upload_2")
        form = wav_files(request.POST)
        
        test.printValue("request.post")
        test.printValue(request.POST)

        test.printValue("request.body")
        test.printValue(body)

        test.printValue(form.is_valid())
        if form.is_valid():
            test.printValue("upload_3")
            files = form.save(commit=False)

            test.printValue(request.FILES)
            
            files.content = request.FILES['content']
           
            files.save()
            test.printValue("upload_4")
            # return redirect('')
            return render(request, 'ruri/main.html')
        


        # body = request.body
        # test.printValue("upload_2")
        # form = wav_files(request.POST)
        
        # test.printValue("request.post")
        # test.printValue(request.POST)

        # test.printValue("request.body")
        # test.printValue(body)

        # test.printValue(form.is_valid())
        # if form.is_valid():
        #     test.printValue("upload_3")
        #     files = form.save(commit=False)

        #     test.printValue(request.FILES)
            
        #     files.content = request.FILES['content']
        #     files.save()
        #     test.printValue("upload_4")
        #     # return redirect('')
        #     return render(request, 'ruri/main.html')


    else:
        form = wav_files()
    context = {
        'form':form
    }
    return render(request, 'ruri/main.html',context)
