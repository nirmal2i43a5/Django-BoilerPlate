

from django.shortcuts import render

def dashboard(request):
    context = {'title': 'Dashboard'}
    return render(request,'dashboard.html', context)

# def home(request):
#     context = {'title': 'Home'}
#     return render(request,'dashboard.html', context)
def error_404(request, exception):
    data = {}
    return render(request,'page-errors/page-404.html', data)