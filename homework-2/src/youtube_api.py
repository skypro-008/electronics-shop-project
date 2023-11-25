import json
import os


from googleapiclient.discovery import build

import isodate
# YT_API_KEY скопирован из гугла и вставлен в переменные окружения
api_key: str = os.getenv('YT_API_KEY')

# создать специальный объект для работы с API
youtube = build('youtube', 'v3', developerKey=api_key)


def printj(dict_to_print: dict) -> None:
    """Выводит словарь в json-подобном удобном формате с отступами"""
    print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))


'''
получить данные о канале по его id
docs: https://developers.google.com/youtube/v3/docs/channels/list

сервис для быстрого получения id канала: https://commentpicker.com/youtube-channel-id.php
'''
# channel_id = 'UC-OVMPlMA3-YCIeg4z5z23A'  # MoscowPython
channel_id = 'UCwHL6WHUarjGfUM_586me8w'  # HighLoad Channel
channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
printj(channel)


'''
получить данные по play-листам канала
docs: https://developers.google.com/youtube/v3/docs/playlists/list
'''
playlists = youtube.playlists().list(channelId=channel_id,
                                     part='contentDetails,snippet',
                                     maxResults=50,
                                     ).execute()
# printj(playlists)
for playlist in playlists['items']:
    print(playlist)
    print()


'''
получить данные по видеороликам в плейлисте
docs: https://developers.google.com/youtube/v3/docs/playlistItems/list

получить id плейлиста можно из браузера, например
https://www.youtube.com/playlist?list=PLH-XmS0lSi_zdhYvcwUfv0N88LQRt6UZn
или из ответа API: см. playlists выше
'''
playlist_id = 'PLH-XmS0lSi_zdhYvcwUfv0N88LQRt6UZn'
playlist_videos = youtube.playlistItems().list(playlistId=playlist_id,
                                               part='contentDetails',
                                               maxResults=50,
                                               ).execute()
# printj(playlist_videos)

# получить все id видеороликов из плейлиста
video_ids: list[str] = [video['contentDetails']['videoId'] for video in playlist_videos['items']]
# print(video_ids)


'''
вывести длительности видеороликов из плейлиста
docs: https://developers.google.com/youtube/v3/docs/videos/list
'''
video_response = youtube.videos().list(part='contentDetails,statistics',
                                       id=','.join(video_ids)
                                       ).execute()
# printj(video_response)

for video in video_response['items']:
    # YouTube video duration is in ISO 8601 format
    iso_8601_duration = video['contentDetails']['duration']
    duration = isodate.parse_duration(iso_8601_duration)
    print(duration)


'''
получить статистику видео по его id
получить id можно из адреса видео
https://www.youtube.com/watch?v=gaoc9MPZ4bw или https://youtu.be/gaoc9MPZ4bw
'''
video_id = 'gaoc9MPZ4bw'
video_response = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                       id=video_id
                                       ).execute()
# printj(video_response)
video_title: str = video_response['items'][0]['snippet']['title']
view_count: int = video_response['items'][0]['statistics']['viewCount']
like_count: int = video_response['items'][0]['statistics']['likeCount']
comment_count: int = video_response['items'][0]['statistics']['commentCount']