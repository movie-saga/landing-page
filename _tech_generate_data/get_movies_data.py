import yaml
import urllib.request
import json
import textwrap

api_key = "aae47f0d"
file_list = [
  "_star-wars.yml",
  "_fast-and-furious.yml"
]

for file_name in file_list:
    with open(file_name, "r") as file:
        movies_ids = yaml.safe_load(file)
    
    file_content = f"""
file_source: {file_name}
movies:
    """

    for movie in movies_ids:
        movie_id = movie["id"]
        url = f"http://www.omdbapi.com/?i={movie_id}&apikey={api_key}"
        movie_detail = urllib.request.urlopen(url).read()
        movie_details_json = json.loads(movie_detail)
        movie_detail_yaml = textwrap.indent(yaml.dump(movie_details_json), prefix="    ")
        movie_detail_yaml = f"""
  - imdb_id: {movie_id}
{movie_detail_yaml}
        """
        file_content += movie_detail_yaml
    
    with open(f"output/{file_name}", "w") as file:
        file.write(file_content)