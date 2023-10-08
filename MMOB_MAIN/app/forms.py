from django import forms
from .models import *


class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = "__all__"


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = "__all__"


class Social_referenceForm(forms.ModelForm):
    class Meta:
        model = Social_reference
        fields = "__all__"


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = "__all__"


class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = "__all__"


class Song_referenceForm(forms.ModelForm):
    class Meta:
        model = Song_reference
        fields = "__all__"
