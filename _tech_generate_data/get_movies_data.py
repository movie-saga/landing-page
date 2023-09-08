import yaml
import urllib.request
import json
import textwrap

api_key = "aae47f0d"
file_list = [
  "_star-wars",
  "_fast-and-furious",
  "_matrix"
]


for file_name in file_list:
    content = []

    with open(f"{file_name}.yml", "r") as file:
        movies_ids = yaml.safe_load(file)

    for movie in movies_ids:
        movie_id = movie["id"]
        url = f"http://www.omdbapi.com/?i={movie_id}&apikey={api_key}"
        movie_detail = urllib.request.urlopen(url).read()
        movie_details_json = json.loads(movie_detail)
        #file_content = json.dumps(movie_details_json, indent=True)
        #movie_details_json["custom_data"] = movie
        movie_details_json = dict(list(movie_details_json.items()) + list(movie.items()))
        content.append(movie_details_json)
        file_content = json.dumps(content, indent=True)
    
    with open(f"../_data/{file_name[1:]}.json", "w") as file:
        file.write(file_content)