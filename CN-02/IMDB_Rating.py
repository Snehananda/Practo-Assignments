import requests


movie_title = input("Enter the movie name: ")
response = requests.get("http://www.omdbapi.com/?t="+movie_title+"&plot=full&apikey=29dd0c39")

json_res = response.json()

print(f"Movie Name: {json_res['Title']}")
print(f"Year: {json_res['Year']}")
print(f"IMDB Rating: {json_res['imdbRating']}")