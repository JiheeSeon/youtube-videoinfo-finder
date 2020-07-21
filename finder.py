from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser
from api_key import DEVELOPER_KEY

## Before you use, make sure to install oauth2client, googleapiclient
## (On the terminal, worked on 2020.07)
## > pip install oauth2client
## > pip install --upgrade google-api-python-client

YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

download_base_url = 'https://www.youtube.com/watch?v='
local_song_list = []


def youtube_search(options, list_name):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)

    search_response = youtube.search().list(
        q=options["q"],
        part="id,snippet",
        maxResults=options["maxResults"]
    ).execute()

    video = {}

    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            video = {"id": search_result["id"]["videoId"], "title": search_result["snippet"]["title"],
                     "url": download_base_url + search_result["id"]["videoId"]}
            list_name.append(video)

    return list_name  # return results with list