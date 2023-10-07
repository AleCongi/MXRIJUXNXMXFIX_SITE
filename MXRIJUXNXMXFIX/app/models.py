from django.db import models

# Create your models here.


class Artist(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Genre(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Social_reference(models.Model):
    id = models.AutoField(primary_key=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    platform = models.CharField(max_length=200)
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Album(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    artist = models.ManyToManyField(Artist)
    release_date = models.DateField()

    def __str__(self):
        return self.name


class Song(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    artist = models.ManyToManyField(Artist)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.name


class Song_reference(models.Model):
    id = models.AutoField(primary_key=True)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    platform = models.CharField(max_length=200)
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Crew(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    artist = models.ManyToManyField(Artist)

    def __str__(self):
        return self.name


class Playlist(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    album = models.ManyToManyField(Album)

    def __str__(self):
        return self.name


class Event(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    artist = models.ManyToManyField(Artist)

    def __str__(self):
        return self.name
