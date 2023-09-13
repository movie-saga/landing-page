import requests
import shutil
import json

file_list = [
  "_star-wars",
  "_fast-and-furious",
  "_matrix"
]

for file_name in file_list:
    with open(f"../_data/{file_name[1:]}.json", "r") as file:
        json_content = json.load(file)

    already_download_posters = []

    for movie in json_content:
        poster = movie["Poster"]
        title = movie["Title"]
        movie_id = movie["id"]
        if poster in already_download_posters:
            continue
        else:
            already_download_posters.append(poster)
        res = requests.get(poster, stream = True)
        if res.status_code == 200:
            with open(f"../assets/img/{movie_id}.jpg",'wb') as f:
                shutil.copyfileobj(res.raw, f)
            print('Image sucessfully Downloaded: ', title)
        else:
            print(f'Image {title} Couldn\'t be retrieved')