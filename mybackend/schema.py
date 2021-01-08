import graphene
from graphene_django import DjangoObjectType
from api.models import Artist, Album, Song

class ArtistType(DjangoObjectType):
    class Meta:
        model = Artist
        fields = ("artist_name", "artist_birthday")

class AlbumType(DjangoObjectType):
    class Meta:
        model = Album
        fields = ("album_name", "publish_date", "artist")

class SongType(DjangoObjectType):
    class Meta:
        model = Song
        fields = ("song_name", "song_playtime", "artist", "album")

class Query(graphene.ObjectType):
    all_artists = graphene.List(ArtistType)
    all_albums = graphene.List(AlbumType)
    all_songs = graphene.List(SongType)

    def resolve_all_artists(root, info):
        return Artist.objects.all()

    def resolve_all_albums(root, info):
        return Album.objects.all()

    def resolve_all_songs(root, info):
        return Song.objects.all()

schema = graphene.Schema(query=Query)