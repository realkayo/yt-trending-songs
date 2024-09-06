from googleapiclient.discovery import build
from discord_webhook import DiscordWebhook
import os
import json

with open(os.path.join('data', 'config.json')) as data:
    json_data = json.load(data)

API_Key = json_data['API_KEY']
yt = build('youtube', 'v3', developerKey=API_Key)

def find_musicas_em_alta(regiao, maxResults):
    res = yt.videos().list(
        part='snippet,statistics',
        chart='mostPopular',
        regionCode=regiao,
        videoCategoryId='10',
        maxResults=maxResults
    ).execute()

    videos_info = []

    for item in res['items']:
        video_title = item['snippet']['title']
        video_id = item['id']
        video_views = item['statistics']['viewCount']
        
        videos_info.append((video_title, video_id, video_views))

    return videos_info


