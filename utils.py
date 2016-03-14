__author__ = 'Frank'
import sys
sys.path.insert(0, 'libs')
from bs4x import BeautifulSoup
from network import *

import json
#html = readFile('home_page.html');
#html = readFile('home_page_nexus4.html');
#html = readUrl('')

def parseHomePage():
    #html = readFile('home_page.html')
    url = 'https://mkito.com'
    html = readUrl(url)
    soup = BeautifulSoup(html, 'html.parser')
    divs = soup.find_all("div", {"class": "col-md-5 col-xs-5 no-padding"})
    songs = []
    for div in divs:
        try:
            # this can get all fucked up really quickly, lets pray
            links = div.find_all('a')

            artist_url = links[0]['href']
            artist_name =links[1].text
            song_url = links[2]['href']
            song_name = links[2]['title']

            image = links[0].img['src']


            c_song = {}
            c_song['song_name'] = song_name
            c_song['image'] = image
            c_song['song_url'] = song_url
            c_song['artist_name'] = artist_name
            c_song['artist_url'] = artist_url

            songs.append(c_song);

        except Exception, e:
            print str(e)
        #break
    return songs

def parseArtistPage(url):
    #html = readFile('a_profile.html')
    html = readUrl(url)
    soup = BeautifulSoup(html, 'html.parser')
    divs = soup.find_all("div", {"class": "albumSongCollections"})
    #print(len(divs))
    songs = []
    for div in divs:
        try:
            # this can get all fucked up really quickly, lets pray
            links = div.find_all('a')
            #for x in links: print('>>>>', x)

            c_song = {}
            c_song['song_url'] = links[0]['href']
            c_song['song_preview'] = links[2]['href']

            #song names can be extracted from urls, the second element from the last and spaces ni -
            s_name = c_song['song_url'].split('/')[-2].replace('-', ' ')
            c_song['song_name'] = s_name



            songs.append(c_song)
        except Exception, e:
            print str(e)
        #break
    return songs

def parseSearch(query):
    # &searchOption=All
    # html = readFile('h.html')
    url =  "https://mkito.com/search/?name="+query.lstrip()
    # print url
    html = readUrl(url)
    soup = BeautifulSoup(html, 'html.parser')
    ass = soup.find_all("a", {"class": "searchHyperLink"})
    songs = []
    # print(len(ass))
    for a in ass:
        try:
            # this can get all fucked up really quickly, lets pray it doesn't
            div = a.find("div", {"class": "search-result"})
            ps = div.find_all('p')
            #for x in ps: print(">>>>", x.text)

            c_song = {}
            c_song['result_url'] = a['href']

            typee = c_song['result_url'].split('/')[3]
            if "song" == typee:
                c_song['result_type'] = 0 # means result is a song
            elif "artist-profile" == typee:
                c_song['result_type'] = 1 # means result is a artist profile
            else:
                continue # the entry wont be added to the list

            c_song['song_name'] = ps[0].text
            c_song['artist_name'] = ps[1].text
            c_song['image'] = div.img['src']


            songs.append(c_song)

        except Exception, e:
            print str(e)
        # break
    return songs

