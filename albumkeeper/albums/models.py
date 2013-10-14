from django.core.urlresolvers import reverse
from django.db import models

class Artist(models.Model):
	name = models.CharField(max_length=40)
	bio = models.TextField()
	pic = models.ImageField(upload_to="albums/artists/%Y/%m/%d", height_field="pic_height", width_field="pic_width")
	pic_height = models.PositiveIntegerField()
	pic_width = models.PositiveIntegerField()
	def __unicode__(self):
		return self.name

class Album(models.Model):
	title = models.CharField(max_length=40)
	artist = models.ForeignKey(Artist)
	year = models.PositiveIntegerField()
	art = models.ImageField(upload_to="albums/album_art/%Y/%m/%d", height_field="art_height", width_field="art_width")
	art_height = models.PositiveIntegerField()
	art_width = models.PositiveIntegerField()
	def __unicode__(self):
		return self.title
	class Meta:
		ordering = ['year','title']

class Song(models.Model):
	title = models.CharField(max_length=100)
	album = models.ForeignKey(Album)
	def __unicode__(self):
		return self.title

class Tag(models.Model):
	albums = models.ManyToManyField(Album)
	name = models.CharField(max_length=40)
	def __unicode__(self):
		return self.name