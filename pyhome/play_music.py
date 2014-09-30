#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    play_music.py

    Starts a playlist. 
    Playlist stored in data/playlist.py

    Usage: called by play.sh [playlist name]
"""    

import sys
from selenium import webdriver

MUSIC = {
'zaz': 'https://www.youtube.com/watch?v=3HzfoQGX3U4&list=PL25D2D0FC0B679AB6&index=2',
'bluesbrothers': 'https://www.youtube.com/watch?v=owCtCy55S2k&list=PL79375DB53E511C2E',
'pulpfiction': 'https://www.youtube.com/watch?v=DZXlZXS9uLU&list=PL91AE989DF30F66AC',
'peterfox': 'https://www.youtube.com/watch?v=Ouuzq8DzHqg&list=PL052A8134A1A2DEFA',
'norahjones':'https://www.youtube.com/watch?v=8UZokFgzKYc',
'bregovic':'https://www.youtube.com/watch?v=vsXsTYfrQIw',
'buenavista':'https://www.youtube.com/watch?v=HaerapRPS64',
'cesaria':'https://www.youtube.com/watch?v=oWYKTiqPvYA',
}

class MusicPlayer:

    def __init__(self):
        self.playlists = MUSIC

    def play(self, name):
        """
        Play given playslist.
        When name is not awailable print s all possibilities.
        """
        if not self.playlists.has_key(name):
            self.show_available()
        else:
            browser = webdriver.Firefox()
            browser.get(self.playlists[name])
            
    def show_available(self):
        """Prints list of available playlists."""
        for li in self.playlists.keys():
            print li

    def stop(self):
        pass



if __name__ == '__main__':
    playm = MusicPlayer()
    if len(sys.argv) > 1:
        name = ''.join(sys.argv[1:])
        name = name.lower()
        if name == 'show':
            playm.show_available()
        else:
            playm.play(name)
        
