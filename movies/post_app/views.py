
# Подключение стандартной формы для регистрации

from django.http import Http404
from django.shortcuts import render, redirect

from .forms import CreateMovieForm
from .models import Movie, Movie_commits


def test1(request):
    dict_ = {
        'title': 'Blog APPLICATION',
        'text': 'HELLO WORLD!',
        'date': ''
    }
    return render(request, 'hellow.html', context=dict_)

def movie_list_view(request):
    movie_list = Movie.objects.all()
    context = {
        'movie': movie_list
    }
    return render(request, 'movie_detail.html', context=context)

def movie_detail_view(request, id):
    try:
        movie_detail = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        raise Http404('movie not FOUND!!!')
    comments = Movie_commits.objects.filter(movies_id=id)
    return render(request, 'movie_list.html', context={
        'detail': movie_detail,
        'comments': comments
    })




def create_movie_view(request):
    form = CreateMovieForm()
    if request.method == 'POST':
        form = CreateMovieForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/movies/')
    return render(request, 'create_movies.html', context={
        'form': form
    })
# Create your views here.
