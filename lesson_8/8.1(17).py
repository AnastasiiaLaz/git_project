class Album:

    def __init__(self, artist, title):
      self.tracks = []
      self.artist = artist
      self.title = title
    def collect(self, track):
      self.tracks.extend(track)


album_1 = Album("Queen", "Killer Queen")
album_1.collect(["Brighton rock", "Killer Queen", "Tenement Funster"])
album_2 = Album(" Metallica", "Black Album")
album_2.collect(["Enter Sandman", "Sad But True", "Holier Than Thou"])
# Не удаляйте этот код, он нужен для проверки

print(album_1.artist, album_1.title, len(album_1.tracks), "треков")
print(album_2.artist, album_2.title, len(album_2.tracks), "треков")