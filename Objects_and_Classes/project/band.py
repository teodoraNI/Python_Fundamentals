from Objects_and_Classes.project.album import Album


class Band:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        else:
            self.albums.append(album)
            return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        if album_name not in self.albums:
            return f"Album {album_name} is not found."
        for album in self.albums:
            if album == album_name and album.published == True:
                return "Album has been published. It cannot be removed."
            elif album.published == False:
                self.albums.remove(album_name)
                return f"Album {album_name} has been removed."
    def details(self):
        result = f"Band {self.name}\n"
        for album in self.albums:
            result += f"{album.details()}\n"
        return result.strip()

