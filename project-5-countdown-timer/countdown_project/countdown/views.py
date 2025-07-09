from django.shortcuts import render
from django.http import StreamingHttpResponse
import time

def set_countdown(seconds):
    yield "Countdown starts now...\n"
    for i in range(seconds, 0, -1):
        yield f'{i:02d}\n'
        time.sleep(1)
    yield "Countdown ended!\n"

def index(request):
    return render(request, 'index.html')

def stream(request):
    seconds = int(request.GET.get('seconds', 10))
    return StreamingHttpResponse(set_countdown(seconds))