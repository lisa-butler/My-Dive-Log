from django.shortcuts import render

# Create your views here.
def get_logpage(request):
    return render(request, "log/logpage.html")
