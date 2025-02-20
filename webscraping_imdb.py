import os
import requests
from bs4 import BeautifulSoup

#the system req or libraries


def download_image(image_url, folder_name, actor_name):
    #os.makedirs(folder_name, exist_ok=True)  
    save_path = os.path.join(folder_name, f"{actor_name}.jpg")  
    response = requests.get(image_url, stream=True)
    if response.status_code == 200:
        with open(save_path, "wb") as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        print(f"Downloaded: {save_path}")


headers = {"User-Agent": "Mozilla/5.0"}


for i in range(10):
    link_no = 50000+i
    url_system = f"https://www.imdb.com/name/nm{link_no:07d}/"
    actor_url = url_system

    print(f"Fetching: {actor_url}")

    
    response = requests.get(actor_url, headers=headers)

   
    soup = BeautifulSoup(response.text, "html.parser")

   
    name_tag = soup.find("h1") 
    if name_tag:
        actor_name = name_tag.text.strip().replace(" ", "_") 

# how to save the code

    image_tag = soup.find("img", class_="ipc-image")
    if image_tag:
        image_url = image_tag["src"] 
        folder_name = f"/content/drive/MyDrive/Celeb_look_like_actor/"  
        download_image(image_url, folder_name, actor_name)  
