from django.contrib import admin
from .models import Artist, Genre, Social_reference, Album, Song, Song_reference
# Register your models here.


admin.site.register(Artist)
admin.site.register(Genre)
admin.site.register(Social_reference)
admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Song_reference)
