import requests
import os
from dotenv import load_dotenv
import json

import re

class Video:
    
    
    def __init__(self, height, width, name, file_name, download_links):
        self.height = height
        self.width = width
        self.name = name
        self.file_name = file_name
        self.download_links = download_links


def download_video(search_term):
    
    pattern = r'video/(.+)/'
    load_dotenv()
    PEXELS_API_KEY = os.getenv("PEXELS_API_KEY")

    headers = {
        "Authorization": PEXELS_API_KEY
    }

    params = {
        "query": search_term,
        "per_page": 50,
        "orientation": "portrait",
        "size" : "large"
    }

    response = requests.get("https://api.pexels.com/videos/search", headers=headers, params=params)

    video_data = response.json()

    video_info = video_data['videos'][0]

    description_url = video_info['url']
    match = re.search(pattern, description_url)
    description = None

    if match:
        description = match.group(1)
        
    collected_videos = []
    total_duration = 0

    for video in video_data['videos']:
        if total_duration + video['duration'] <= 60:
            collected_videos.append(video['video_files'][0]['link'])
            total_duration += video['duration']
        if total_duration >= 60:
            break
    
    video_url = video_info['video_files'][0]['link']
    height, width = video_info['video_files'][0]['height'], video_info['video_files'][0]['width']
    name = video_info['user']['name']
    file_name = '{}.{}'.format(description, 'mp4') 

    editing_info = Video(height, width, name, file_name, collected_videos)
    
    new_term = search_term.replace(" ", "_")
    parent_directory = 'src/source_video'
    directory_path = os.path.join(parent_directory, new_term)
    
    if not os.path.exists(parent_directory):
        os.makedirs(parent_directory)
    
    if not os.path.exists(directory_path):
        os.mkdir(directory_path)
    
    for i, link in enumerate(collected_videos):
        video_response = requests.get(link)
        this_video_name = 'src/source_video/{}/{}_{}.mp4'.format(new_term, i, editing_info.name)
        with open(this_video_name, 'wb') as f:
            f.write(video_response.content)
    
    print('progress: videos downloaded')
    return editing_info