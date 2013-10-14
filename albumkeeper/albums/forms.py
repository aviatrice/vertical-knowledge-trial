from django.forms import ModelForm, TextInput, Textarea, FileInput, Select
from django.forms.models import inlineformset_factory, modelformset_factory
from albums.models import Artist, Album, Song

class ArtistForm(ModelForm):
	class Meta:
		model = Artist
		fields = ['name', 'bio', 'pic']
		widgets = {
			'name':TextInput(attrs={'class':'form-control'}),
			'bio':Textarea(attrs={'class':'form-control'}),
		}

class AlbumForm(ModelForm):
	class Meta:
		model = Album
		fields = ['id', 'artist', 'title', 'year', 'art']
		widgets = {
			'id':TextInput(attrs={'class':'hidden'}),
			'artist':Select(attrs={'class':'form-control'}),
			'title':TextInput(attrs={'class':'form-control'}),
			'year':TextInput(attrs={'class':'form-control'}),
		}

class SongForm(ModelForm):
	class Meta:
		model = Song
		widgets = {
			'title':TextInput(attrs={'class':'form-control'}),
		}

AlbumFormSet = modelformset_factory(Album, form=AlbumForm)