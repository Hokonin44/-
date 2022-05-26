
from django.contrib import admin
from .models import Director, Movie, Movie_commits, Tag


class CommentInine(admin.StackedOnline):
    model = Movie_commits
    extra = 0


class MoviesAdmin(admin.ModelAdmin):
    list_display = 'id title descriptions'.split()
    search_fields = 'title '.split()
    list_filter = 'tags'.split()


admin.site.register(Director)
admin.site.register(Movie, MoviesAdmin)
admin.site.register(Movie_commits)
admin.site.register(Tag)
