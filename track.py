class Track:
    """music"""

    def __init__(self, name, id, artist, image):

        self.name = name
        self.id = id
        self.artist = artist
        self.image = image

    def create_spotify_uri(self):
        return f"spotify:track:{self.id}"

    def __gt__(self, other):
        return True



    def __str__(self):
        return f"{self.name} by {self.artist}"