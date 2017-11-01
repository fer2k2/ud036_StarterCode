# Using utf-8 since we don't want problems with non-english names
# coding=utf-8

from media import Movie
import fresh_tomatoes
import csv

movies = []  # Movies list


def main():  # Wrapping everything in a main function

    # Open the csv file in the same directory with the movies info
    with open('movies.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=';', quotechar='"')
        i = 0  # Variable to avoid the header row
        for row in reader:
            if i == 0:
                i += 1
            else:
                temp_movie = Movie(row)  # Create a Movie instance
                movies.append(temp_movie)  # Append the movie to the list

    fresh_tomatoes.open_movies_page(movies)  # Generate and open web page


if __name__ == "__main__":
    main()
