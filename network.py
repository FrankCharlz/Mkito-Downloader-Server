__author__ = 'Frank'
import urllib
import urllib2

USER_AGENT = 'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.122 Mobile Safari/537.36'

def readUrl(url):
    values = {}
    headers = {'User-Agent': USER_AGENT}

    data = urllib.urlencode(values)
    req = urllib2.Request(url, data, headers)
    response = urllib2.urlopen(req)
    content = response.read()
    return content

def readFile(path):
    f = open(path, 'r')
    data = f.read()
    f.close()
    return data

