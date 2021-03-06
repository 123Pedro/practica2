from django.db import  models

class Album(models.model):
    artist=models.CharField(max_length=250)
    album_title=models.CharField(max_length=500)
    genro=models.CharField(max_length=100)
    album_logo=models.CharField(max_length=1000)

class Song(models.model):
   album=models.ForeignKey(Album,on_delete=models.CASCADE)
    file_type=models.CharField(max_length=20)
    song_title=models.CharField(max_length=250)