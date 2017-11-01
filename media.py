class Movie:
    """
    This class defines a movie with all his properties
    """

    def __init__(self, movie_data):
        self.title = movie_data[0]
        self.duration = movie_data[1]
        self.year = movie_data[2]
        self.director = movie_data[3]
        self.poster_image_url = movie_data[4]
        self.trailer_youtube_url = movie_data[5]

