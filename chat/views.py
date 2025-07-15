from django.shortcuts import render

def chat(request):
    return render(request, 'chat/chat.html')
def index(request):
    return render(request, 'chat/index.html')