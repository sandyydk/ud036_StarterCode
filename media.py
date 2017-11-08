import webbrowser
from video import Video


class Movie(Video):
    """ This class provides away to store movie related information """
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube, duration):
        Video.__init__(self, movie_title, duration, movie_storyline)
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Ununsed now.Can be used to directly launch trailer of a movie"""
        webbrowser.open(self.trailer_youtube_url)
