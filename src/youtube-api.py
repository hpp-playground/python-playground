import os
import requests

API_KEY = os.environ['YOUTUBE_API_KEY']
ACCESS_TOKEN = os.environ['YOUTUBE_ACCESS_TOKEN']
CHANNEL_ID = 'UCD-miitqNY3nyukJ4Fnf4_A'

url = 'https://www.googleapis.com/youtube/v3/search'
infos = []

print(API_KEY, CHANNEL_ID, url, infos)

params = {
    "key": API_KEY,
    "channelId": CHANNEL_ID,
    "part": "snippet",
    "order": "date",
    "maxResults": 50,
}


response = requests.get(url, params=params)
print(response)
result = response.json()

video_ids = []

for item in result["items"]:
    print(item["id"])
    if item["id"]["kind"] == "youtube#video":
        video_ids.append(item["id"]["videoId"])

print(video_ids)

url = "https://www.googleapis.com/youtube/v3/captions"
caption_ids = []

for video_id in video_ids:
    params = {
        "videoId": video_id,
        "key": API_KEY,
        "tfmt": "ttml",
        "part": "snippet",
    }
    response = requests.get(url, params=params)
    print(response)
    result = response.json()
    print(result)
    for item in result["items"]:
        caption_ids.append(item["id"])

print(caption_ids)

caption_data = []
headers = {'Authorization': 'Bearer ' + ACCESS_TOKEN}

for caption_id in caption_ids:
    url = "https://www.googleapis.com/youtube/v3/captions/" + caption_id
    params = {
        "key": API_KEY,
        "tfmt": "ttml",
    }
    print(url)
    try:
        response = requests.post(url, params=params, headers=headers)
        print(response)
        result = response.json()
        print(result)
    except :
        print("Error")
