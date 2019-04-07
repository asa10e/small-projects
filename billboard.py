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
    billboard_site = 'https://www.billboard.com/charts/hot-100'
    html = requests.get(billboard_site).text
    soup = BeautifulSoup(html, 'html.parser')

    div = soup.find('div', {'class': 'chart-list-item', 'data-rank':'1'})
    artist = div['data-artist']
    song_title = div['data-title']

    combined_data = artist + ' ' + song_title # What we'll search YouTube for

    return combined_data


def text_to_video(text):
    """
    Searches youtube for the given text and returns the url
    of the first resulting video.
    """
    query = urllib.parse.quote(text) # "hello world" -> "hello%20world", etc.
    url = 'https://www.youtube.com/results?search_query=' + query
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
