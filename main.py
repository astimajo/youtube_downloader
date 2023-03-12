# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 17:26:50 2023

@author: Angelo Timajo (modified from geeksforgeeks)
"""

from pytube import YouTube
import os
from tqdm import tqdm
import time

# PUT ALL URLS HERE.

urls = [] # Input all URLs here as strings.

# FUNCTION PROPER
    
def youtube_downloader(urls: list, only_audio:bool=True):
    """Downloads youtube media files from urls."""
    for url in tqdm(urls):
        try:
            # url input from user
            yt = YouTube(url)
              
            # extract only audio
            video = yt.streams.filter(only_audio=only_audio).first()
              
            # check for destination to save file
            destination = '.'
              
            # download the file
            out_file = video.download(output_path=destination)
              
            # save the file
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
            print()
            # result of success
            print(yt.title + " has been successfully downloaded.")
            print()
            print('Script sleeping for 10 seconds to refresh...')
            time.sleep(10)
            
        except:
            print()
            print(f'File already exist for link: {url}.')
            continue

# FUNCTION USAGE
youtube_downloader(urls)