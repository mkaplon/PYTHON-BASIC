import requests
import json
import os
import threading
from concurrent.futures import ThreadPoolExecutor

API_KEY = "my_API"
APOD_ENDPOINT = 'https://api.nasa.gov/planetary/apod'
OUTPUT_IMAGES = './output'

thread_local = threading.local()

def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session

def get_apod_metadata(start_date: str, end_date: str, api_key: str) -> list:
    url = f"{APOD_ENDPOINT}?api_key={api_key}&start_date={start_date}&end_date={end_date}"
    page = requests.get(url=url)
    data = json.loads(page.text)
    return data


def download_image(image: dict):
    if image["media_type"] == "image":
        with open(f"{OUTPUT_IMAGES}/{image['date']}.jpg", "wb") as file:
            session = get_session()
            with session.get(image["url"]) as response:
                file.write(response.content)


def download_apod_images(metadata: list):
    with ThreadPoolExecutor(max_workers=15) as ex:
        ex.map(download_image, metadata)


def main():
    metadata = get_apod_metadata(
        start_date='2021-08-01',
        end_date='2021-09-30',
        api_key=API_KEY,
    )
    download_apod_images(metadata=metadata)


if __name__ == '__main__':
    if not os.path.exists(OUTPUT_IMAGES):
        os.makedirs(OUTPUT_IMAGES)

    main()
