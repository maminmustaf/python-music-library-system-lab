#!/usr/bin/env python3


class Song:
    count = 0
    genres = set()
    artists = set()
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # Count total songs
        Song.count += 1

        # Keep track of genres
        Song.genres.add(genre)

        # Keep track of artists
        Song.artists.add(artist)

        # Count songs by genre
        if genre not in Song.genre_count:
            Song.genre_count[genre] = 0
        Song.genre_count[genre] += 1

        # Count songs by artist
        if artist not in Song.artist_count:
            Song.artist_count[artist] = 0
        Song.artist_count[artist] += 1