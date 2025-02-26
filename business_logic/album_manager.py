import os

import model
import data_access


class AlbumManager():
    def __init__(self) -> None:
        self.__album_dal = data_access.AlbumDAL()

    def create_album(self, title: str, artist: model.Artist = None) -> model.Album:
        return self.__album_dal.create_new_album(title, artist)

    def read_artists_albums(self, artist: model.Artist) -> None:
        self.__album_dal.read_albums_by_artist(artist)

    def read_album(self, album_id: int) -> model.Album:
        return self.__album_dal.read_album_by_id(album_id)
