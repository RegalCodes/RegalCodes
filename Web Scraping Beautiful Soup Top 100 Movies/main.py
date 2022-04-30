import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"


response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_movies = soup.find_all(name="h3", class_="title")

movie_titles = [movie.getText() for movie in all_movies]
#movie is each item in the list, and the new item is what you want to get from each item in the list.

movies = movie_titles[::-1]

with open("movies.text", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")

#this makes it a list and prints it out 1 at a time.
# for n in range(len(movie_titles) -1, 0, -1):
#     print(movie_titles[n])