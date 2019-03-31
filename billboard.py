import requests
import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver

import re
import time


def find_top_song():
    """
    Grabs the title and artist of the top song on the Billboard Hot 100.
    """
    billboard_site = "https://www.billboard.com/charts/hot-100"
    html = requests.get(billboard_site).text
    soup = BeautifulSoup(html, 'html.parser')
    all_songs = soup.find("div", {"class": "chart-list chart-details__left-rail"})

    text_before_song = """<div class="chart-list chart-details__left-rail" data-video-playlist="[{&quot;id&quot;:&quot;6017857746001&quot;,&quot;rank&quot;:1,&quot;title&quot;:&quot;"""
    text_after_song = "&quot;"
    song = (str(all_songs).split(text_before_song))[1].split(text_after_song)[0] # Text between text_before_song and text_after_song

    return song


def text_to_video(text):
    """
    Searches youtube for the given text and returns the url
    of the first resulting video.
    """
    query = urllib.parse.quote(text) # "hello world" -> "hello%20world", etc.
    url = "https://www.youtube.com/results?search_query=" + query
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    topvid = soup.findAll(attrs={'class':'yt-uix-tile-link'})[0]
    topvid_url = 'https://www.youtube.com' + topvid['href']

    return topvid_url


def find_and_play_top_song():
    """
    Opens a webdriver and plays Billboard's top song on youtube.
    """
    driver = webdriver.Chrome()

    song = find_top_song()
    vid_link = text_to_video(song)
    driver.get(vid_link)

    time.sleep(3600) # Close window automatically after a while
    driver.close()

    return None


if __name__ == '__main__':
    find_and_play_top_song()
