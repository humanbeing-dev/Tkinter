"""Application for reading youtube playlists"""
from tkinter import *
import re
import os
from datetime import timedelta
from googleapiclient.discovery import build
from dotenv import load_dotenv
load_dotenv()


def get_playlist_title_and_description(pl_id):
    youtube = build('youtube', 'v3', developerKey=os.getenv("api_key"))
    pl_request = youtube.playlists().list(
        part='snippet',
        id=pl_id,
    )

    pl_response = pl_request.execute()

    pl_title = pl_response['items'][0]['snippet']['title']
    pl_desc = pl_response['items'][0]['snippet']['description']

    return {"pl_title": pl_title, "pl_desc": pl_desc}


def get_videos_urls_from_playlist(pl_id):
    """Function that takes playlistId and returns list of videosIds of this playlist"""
    youtube = build('youtube', 'v3', developerKey=os.getenv("api_key"))
    next_page_token = None
    vid_ids = []
    while True:
        pl_request = youtube.playlistItems().list(
            part='contentDetails',
            playlistId=pl_id,
            maxResults=50,
            pageToken=next_page_token
        )

        pl_response = pl_request.execute()
        movies = pl_response['items']

        for movie in movies:
            vid_ids.append(movie['contentDetails']['videoId'])

        next_page_token = pl_response.get('nextPageToken')
        if not next_page_token:
            break

    return [pl_id, vid_ids]


def get_videos_data(videoList):
    youtube = build('youtube', 'v3', developerKey=os.getenv("api_key"))
    playlistId = videoList[0]
    videoList = videoList[1]
    vid_data = []

    while videoList:
        vid_current, videoList = videoList[:50], videoList[50:]

        vid_request = youtube.videos().list(
            part='contentDetails, snippet',
            id=vid_current
        )

        vid_response = vid_request.execute()

        hours_pattern = re.compile(r'(\d+)H')
        minutes_pattern = re.compile(r'(\d+)M')
        seconds_pattern = re.compile(r'(\d+)S')

        for item in vid_response['items']:
            vid_id = item['id']
            vid_len = item['contentDetails']['duration']

            hours = hours_pattern.search(vid_len)
            minutes = minutes_pattern.search(vid_len)
            seconds = seconds_pattern.search(vid_len)

            hours = int(hours.group(1)) if hours else 0
            minutes = int(minutes.group(1)) if minutes else 0
            seconds = int(seconds.group(1)) if seconds else 0

            video_seconds = timedelta(
                hours=hours, minutes=minutes, seconds=seconds).total_seconds()

            vid_title = item['snippet']['title']
            vid_desc = item['snippet']['description']
            vid_published_date = item['snippet']['publishedAt']

            vid_data.append({"vid_id": vid_id,
                             "vid_length": video_seconds,
                             "vid_title": vid_title,
                             "vid_desc": vid_desc,
                             "vid_published_date": vid_published_date})

    return vid_data






