from django.conf import settings
from django.conf.urls import patterns, url
from django.conf.urls.static import static

from albums import views

urlpatterns = patterns(
	'',
	url(r'^$', views.ArtistView.as_view(), name='index'),
	url(r'^album/add/$', views.album_create, name='album_add'),
	url(r'^album/(?P<pk>\d+)/edit/$', views.album_edit, name='album_update'),
	url(r'^album/(?P<pk>\d+)/delete/$', views.AlbumDelete.as_view(), name='album_delete'),
	url(r'^album/(?P<pk>\d+)/', views.AlbumDetail.as_view(), name='album_detail'),
	url(r'^artists/$', views.ArtistView.as_view(), name='artists'),
	url(r'^tags/$', views.TagView.as_view(), name='tags'),
	url(r'^artist/add/$', views.ArtistCreate.as_view(), name='artist_add'),
	url(r'^artist/(?P<pk>\d+)/edit/$', views.ArtistUpdate.as_view(), name='artist_update'),
	url(r'^artist/(?P<pk>\d+)/delete/$', views.ArtistDelete.as_view(), name='artist_delete'),
	url(r'^artist/(?P<pk>\d+)/', views.ArtistDetail.as_view(), name='artist_detail'),
)