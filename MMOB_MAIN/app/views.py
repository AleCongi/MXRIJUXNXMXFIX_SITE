from django.shortcuts import redirect, render, get_object_or_404
from django.db.models import F

from .forms import *
from .models import *

# create a homepage view calling the template homepage.html


def homepage(request):
    return render(request, 'homepage.html')


'''

# GENERE


def Genre_list(request):
    Genres = Genre.objects.all()
    return render(request, 'Genre_list.html', {'Genres': Genres})

# CREW


def Crew_detail(request, Crew_id):
    Crew = get_object_or_404(Crew, id=Crew_id)
    return render(request, 'Crew_detail.html', {'Crew': Crew})

# ARTIST


def Artist_list(request):
    Artists = Artist.objects.all()
    return render(request, 'Artist_list.html', {'Artists': Artists})


def Artist_detail(request, Artist_id):
    Artist = get_object_or_404(Artist, id=Artist_id)
    Social_references = Artist.social_reference_set.all()
    Crews = Artist.crew_set.all()
    Albums = Artist.album_set.all()
    return render(request, 'Artist_detail.html',
                  {'Artist': Artist,
                   'Crews': Crews,
                   'Social_references': Social_references,
                   'Albums': Albums})


# PLAYLIST
def Playlist_list(request):
    Playlists = Playlist.objects.all()
    return render(request, 'Playlist_list.html', {'Playlists': Playlists})


def Playlist_detail(request, Playlist_id):
    Playlist = get_object_or_404(Playlist, id=Playlist_id)
    return render(request, 'Playlist_detail.html', {'Playlist': Playlist})


# SONGS
def song_list(request):
    songs = Song.objects.all()
    return render(request, 'song_list.html', {'songs': songs})


def song_list_by_artist(request, artist_id):
    artist = get_object_or_404(Artist, id=artist_id)
    songs = artist.song_set.all()
    return render(request, 'song_list.html', {'songs': songs})


def song_list_by_album(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    songs = album.song_set.all()
    return render(request, 'song_list.html', {'songs': songs})


def song_list_by_genre(request, genre_id):
    genre = get_object_or_404(Genre, id=genre_id)
    songs = genre.song_set.all()
    return render(request, 'song_list.html', {'songs': songs})


def song_detail(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    return render(request, 'song_detail.html', {'song': song})









def collection_detail(request, collection_id):
    collection = get_object_or_404(Collection, id=collection_id)
    return render(request, 'collection_detail.html', {'collection': collection})

def manga_volume_list(request):
    manga_volumes = MangaVolume.objects.all()
    return render(request, 'manga_volume_list.html', {'manga_volumes': manga_volumes})

def homepage(request):
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    
    # Check if the user agent indicates a mobile device
    is_mobile = 'Mobile' in user_agent or 'Android' in user_agent
    if is_mobile:
        template_name = 'default.html'
    else:
        template_name = 'desktop_homepage.html'
    
    collections = Collection.objects.annotate(
        is_favorite=F('favorite')
    ).order_by('-is_favorite', 'name')
    
    return render(request, template_name, {'collections': collections})

def update_volumes(request, collection_id):
    if request.method == 'POST':
        collection = get_object_or_404(Collection, id=collection_id)
        volume_ids = request.POST.getlist('volumes')
        
        for volume in collection.mangavolume_set.all():
            if str(volume.id) in volume_ids:
                volume.owned = True
            else:
                volume.owned = False
            volume.save()

        # Gestione del campo 'favorite'
        favorite = request.POST.get('favorite')
        if favorite is None:
            collection.favorite = False
        elif favorite == '1':
            collection.favorite = True
        else:
            collection.favorite = False
        collection.save()
        collection.update_completion_percentage()
        
    return redirect('collection_detail', collection_id=collection_id)

def add_collection(request):
    if request.method == 'POST':
        form = CollectionForm(request.POST, request.FILES)
        if form.is_valid():
            collection = form.save(commit=False)

            author_name = request.POST.get('author')
            new_author_name = request.POST.get('new_author')
            if author_name:
                try:
                    collection.author = Author.objects.get(name=author_name)
                except Author.DoesNotExist:
                    # Gestione se l'autore non esiste nel database
                    pass
            elif new_author_name:
                new_author = Author.objects.create(name=new_author_name)
                collection.author = new_author

            publisher_name = request.POST.get('publisher')
            new_publisher_name = request.POST.get('new_publisher')
            if publisher_name:
                try:
                    collection.publisher = Publisher.objects.get(name=publisher_name)
                except Publisher.DoesNotExist:
                    # Gestione se l'editore non esiste nel database
                    pass
            elif new_publisher_name:
                new_publisher = Publisher.objects.create(name=new_publisher_name)
                collection.publisher = new_publisher

            genre_name = request.POST.get('genre')
            new_genre_name = request.POST.get('new_genre')
            if genre_name:
                try:
                    collection.genre = Genre.objects.get(name=genre_name)
                except Genre.DoesNotExist:
                    # Gestione se il genere non esiste nel database
                    pass
            elif new_genre_name:
                new_genre = Genre.objects.create(name=new_genre_name)
                collection.genre = new_genre

            collection.save()
            return redirect('collection_detail', collection_id=collection.id)
    else:
        form = CollectionForm()

    context = {'form': form}
    return render(request, 'add_collection.html', context)

def delete_collection(request, collection_id):
    collection = get_object_or_404(Collection, id=collection_id)
    
    if request.method == 'POST':
        if request.POST.get('confirm') == 'yes':
            collection.delete()
            return redirect('homepage')  # Reindirizza verso l'homepage
    
    return render(request, 'delete_collection.html', {'collection': collection})

def edit_collection(request, collection_id):
    collection = get_object_or_404(Collection, id=collection_id)

    if request.method == 'POST':
        form = CollectionForm(request.POST, request.FILES, instance=collection)
        if form.is_valid():
            form.save()
            return redirect('collection_detail', collection_id=collection.id)
    else:
        form = CollectionForm(instance=collection)

    context = {'form': form}
    return render(request, 'edit_collection.html', context)

def support(request):
    return render(request, 'support.html')

def profilo(request):
    return render(request, 'profilo.html')
'''
