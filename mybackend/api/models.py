from django.db import models

class Artist(models.Model):
    artist_name = models.CharField(max_length=50)
    artist_birthday = models.DateField("birthday")

    def __str__(self):
      return self.artist_name

class Album(models.Model):
    album_name = models.CharField(max_length=50)
    publish_date = models.DateField("release date")
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
      return self.album_name

class Song(models.Model):
    song_name = models.CharField(max_length=50)
    song_playtime = models.CharField(max_length=50)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
      return self.song_name