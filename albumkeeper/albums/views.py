from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.views import generic
from albums.forms import ArtistForm, AlbumForm
from albums.models import Artist, Album, Song, Tag

class ArtistView(generic.ListView):
	model = Artist
	template_name = 'albums/artists.html'

class TagView(generic.ListView):
	model = Tag
	template_name = 'albums/tags.html'

class AlbumDetail(generic.DetailView):
	model = Album

class ArtistDetail(generic.DetailView):
	model = Artist

class ArtistCreate(generic.edit.CreateView):
	model = Artist
	form_class = ArtistForm
	success_url = reverse_lazy('albums:artists')

class ArtistUpdate(generic.edit.UpdateView):
	model = Artist
	form_class = ArtistForm
	success_url = reverse_lazy('albums:artists')

class ArtistDelete(generic.edit.DeleteView):
	model = Artist
	success_url = reverse_lazy('albums:artists')

class AlbumDelete(generic.edit.DeleteView):
	model = Album
	success_url = reverse_lazy('albums:artists')

def album_create(request):
	if request.method == 'POST':
		form = AlbumForm(request.POST, request.FILES)
		if form.is_valid():
			# save album
			album = form.save()
			# save tags
			tags = request.POST['tags'].split(", ")
			for tag_name in tags:
				tag = Tag.objects.filter(name__iexact=tag_name)
				if tag:
					tag = tag[0]
				else:
					tag = Tag(name=tag_name)
					tag.save()
				tag.albums.add(album)
				tag.save()
			# save songs
			index = 0
			while 'song_set-'+str(index)+'-title' in request.POST:
				title = request.POST['song_set-'+str(index)+'-title']
				if title!="":
					song = Song(title=title, album=album)
					song.save()
				index += 1
			return redirect('albums:artists');
	else:
		form = AlbumForm()
	return render_to_response('albums/album_form.html', {'form':form}, context_instance=RequestContext(request))

def album_edit(request, pk):
	if request.method == 'POST':
		form = AlbumForm(request.POST, request.FILES)
		if form.is_valid():
			# save album
			album = form.save()
			# save tags
			tags = request.POST['tags'].split(", ")
			for tag_name in tags:
				tag = Tag.objects.filter(name__iexact=tag_name)
				if tag:
					tag = tag[0]
				else:
					tag = Tag(name=tag_name)
					tag.save()
				if album not in tag.albums.all():
					tag.albums.add(album)
					tag.save()
			# save songs
			for song in album.song_set.all():
				song.remove()
			index = 0
			while 'song_set-'+str(index)+'-title' in request.POST:
				title = request.POST['song_set-'+str(index)+'-title']
				if title!="":
					song = Song(title=title, album=album)
					song.save()
				index += 1
			return redirect('albums:artists');
	else:
		album = Album.objects.get(pk=pk)
		if album:
			form = AlbumForm(instance=album)
			song_set = album.song_set.all()
			tag_set = album.tag_set.all()
			tags = []
			for tag in tag_set:
				tags.append(tag.name)
			tags = ", ".join(tags)
			return render_to_response('albums/album_form.html', {'form':form,'tags':tags, 'song_set':song_set}, context_instance=RequestContext(request))
		else:
			form = AlbumForm()
			return render_to_response('albums/album_form.html', {'form':form}, context_instance=RequestContext(request))
	return render_to_response('albums/album_form.html', {'form':form}, context_instance=RequestContext(request))