from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required()
def index_view(request):
    html = 'index.html'
    return render(request,html)
