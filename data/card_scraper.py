import json
import os
import requests
import time 

def download_image(url, save_path):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(save_path, 'wb') as f:
                f.write(response.content)
            print(f"Downloaded: {url}")
        else:
            print(f"Failed to download: {url} (Status Code: {response.status_code})")
    except Exception as e:
        print(f"Error downloading {url}: {str(e)}")

json_file = "oracle.json"

if os.path.exists(json_file):

    with open('oracle.json', 'r', encoding="utf8") as f:
        oracle = json.load(f)
    os.makedirs("imgs", exist_ok=True)
    for card in oracle:
        try:
            image_filename = f"imgs/{card['id']}.jpg"
            download_image(card["image_uris"]["normal"], image_filename)
            time.sleep(0.11)
        except Exception as e:
            print(f"Error downloading {card['name']}: {str(e)}")
else:
    print(f"JSON file '{json_file}' not found.")

print("Download process completed.")