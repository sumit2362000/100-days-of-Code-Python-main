
from bs4 import BeautifulSoup
import requests
import re

URL = 'https://www.empireonline.com/movies/features/best-movies-2/'
 
soup = BeautifulSoup(requests.get(URL).text, 'html.parser')
site_data = str(soup.find(id="__NEXT_DATA__").contents[0])
 
start_indexes = [occurrence.start() + 13 for occurrence in re.finditer('"titleText":"', site_data)]
print(start_indexes)
# The + 13 gives us the index of the start of the film-title
 
for start_index in start_indexes[::-1]:
 
    end_index = site_data.find('"', start_index)
    title = site_data[start_index:end_index]
 
    try:
        file = open('movies.txt', 'a')
    except FileNotFoundError:
        file = open('movies.txt', 'w')
    finally:
        file.write(f"{title}\n")
        file.close()



# URL = "https://www.empireonline.com/movies/features/best-movies-2/"

# response = requests.get(URL)
# website_html = response.text

# soup = BeautifulSoup(website_html, "html.parser")

# all_movies = soup.find_all(name="h3", class_="title")

# movie_titles = [movie.getText() for movie in all_movies]
# movies = movie_titles[::-1]

# with open("movies.txt", mode="w") as file:
#     for movie in movies:
#         file.write(f"{movie}\n")