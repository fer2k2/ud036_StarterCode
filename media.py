class Movie:
    """
    This class defines a movie with all his properties
    """
    def __init__(self, title, duration, year, director, poster_image_url, trailer_youtube_url):
        self.title = title
        self.duration = duration
        self.year = year
        self.director = director
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
