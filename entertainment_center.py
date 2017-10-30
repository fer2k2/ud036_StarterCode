# Using utf-8 since we don't want problems with non-english names
# coding=utf-8

from media import Movie
import fresh_tomatoes

movies = [] # Movies list

# Wrapping everything in a main function
def main():

    amores = Movie("Amores Perros", 154, 2000, "Alejandro González Iñárritu", "https://images-na.ssl-images-amazon.com/images/M/MV5BZjYwYzliYTktMzk3MS00MzE0LTllM2QtMDk3MTFmOGQ2MjE0XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg", "https://www.youtube.com/watch?v=xvwk-xYZcr0")
    innocence = Movie("Innocence", 122, 2004, "Lucile Hadzihalilovic", "https://images-na.ssl-images-amazon.com/images/M/MV5BNzY1MjM4Mzg1NF5BMl5BanBnXkFtZTcwNDEyNjkzMQ@@._V1_.jpg", "https://www.youtube.com/watch?v=V05v-8MnNw0")
    raw = Movie("Raw", 99, 2016, "Julia Ducournau","https://images-na.ssl-images-amazon.com/images/M/MV5BMTU3MDUxMDI0MV5BMl5BanBnXkFtZTgwMzk3OTg3MDI@._V1_SY1000_CR0,0,674,1000_AL_.jpg","https://www.youtube.com/watch?v=udkwT3p28Sw")

    movies.append(amores)
    movies.append(innocence)
    movies.append(raw)

    fresh_tomatoes.open_movies_page(movies)


if __name__ == "__main__": main()