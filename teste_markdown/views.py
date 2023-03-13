from django.http import HttpResponse
from django.shortcuts import render
from .forms import TesteForm

def get_name(request):
    if request.method == 'POST':
        form = TesteForm(request.POST)
        if form.is_valid():
            return HttpResponse(content='OK')
    else:
        form = TesteForm()

    return render(request, 'index.html', {'form': form})