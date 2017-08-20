from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie
from .forms import MovieForm
# Create your views here.
def index(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save()
            movies = Movie.objects.filter(username = movie.username)
            # movies = Movie.objects.all()
            return render(request, 'kp_upload_movie/file_uploaded.html', {
                'movies':movies
            })
    else:
        form = MovieForm()
    return render(request, 'kp_upload_movie/index.html', {
        'form':form,
        })
