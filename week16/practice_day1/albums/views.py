from django.shortcuts import render, redirect
from .models import Album
from .forms import AlbumForm

# Create your views here.
def create(request):
    form = AlbumForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('album:index')
    

def index(request):
    context = {
        'albums': Album.objects.all(),
        'form': AlbumForm(),
    }
    return render(request, 'index.html', context)