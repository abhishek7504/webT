import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','WebT.settings')
import django
django.setup()
from video.models import Video
import requests

def dataupdate():
    GOOGLE_API_KEY = "AIzaSyDGP9iLwxdg_ebyg9pqpya_RjVNqyKkgtg"
    CHANNEL_ID = "UC2nd2XJDCPRY5h2K8QZ8cIQ"
    MAXRESULTS = 50
    myArray = []
    GET_URL = "https://www.googleapis.com/youtube/v3/search?key={}&channelId={}&part=snippet,id&order=date&maxResults={}".format(GOOGLE_API_KEY, CHANNEL_ID, MAXRESULTS)
    url = GET_URL
    while True:
        response = requests.get(url)
        response = response.json()
        # print(response)
        for items in response['items']:
            if items['id']['kind'] == 'youtube#video':
                video_id = items['id']['videoId']
                iframe = '<iframe width="560" height="315" src="https://www.youtube.com/embed/{}" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'.format(video_id)
                Video.objects.get_or_create(title=items['snippet']['title'],
                                     Description=items['snippet']['description'],
                                     Embed_code=iframe,
                                     )
                # print(video_id)
        try:
            next_page_token = response['nextPageToken']
            url = GET_URL + '&pageToken={}'.format(next_page_token)
        except Exception as e:
                print(e)


dataupdate()