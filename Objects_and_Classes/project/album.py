from Objects_and_Classes.project.song import Song


class Album:
    def __init__(self, name: str, *songs, published = False):
        self.name = name
        self.songs = list(songs)
        self.published = published

    def add_song(self, song: Song):
        if song.single == True:
            return f"Cannot add {song.name}. It's a single"
        if self.published == True:
            return "Cannot add songs. Album is published."
        if song in self.songs:
            return "Song is already in the album."
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        if self.published == True:
            return "Cannot remove songs. Album is published."
        if song_name not in self.songs:
            return "Song is not in the album."
        else:
            self.songs.remove(song_name)
            return f"Removed song {song_name} from album {self.name}."

    def publish(self):
        if self.published == True:
            return f"Album {self.name} is already published."
        else:
            self.published = True
            return f"Album {self.name} has been published."

    def details(self):
        result = f"Album {self.name}\n"
        for song in self.songs:
            result += f"== {song.get_info()}\n"
        return result.strip()

