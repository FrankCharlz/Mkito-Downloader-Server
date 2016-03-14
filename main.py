import sys
sys.path.insert(0, 'libs')

import webapp2
from  utils import *

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('<a href=/home>HOME EXAMPLE</a><br>')
        self.response.write('<a href=/artist?page_url=//mkito.com/artist-profile/mwana-fa/937>ARTIST EXAMPLE</a>')

class HomeHandler(webapp2.RequestHandler):
    def get(self):
        result = {}
        try:
            songs = parseHomePage()
            result['songs'] = songs
            result['success'] = 1
        except:
            result['success'] = 0

        self.response.cache_control = 'public'
        self.response.cache_control.max_age = 3600 #1 hour
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(json.dumps(result, indent=4))

class ArtistHandler(webapp2.RequestHandler):
    def get(self):
        page_url = self.request.get('page_url')

        #format of url
        #//mkito.com/artist-profile/mwana-fa/937
        result = {}

        try:
            songs = parseArtistPage('https:'+page_url)
            result['songs'] = songs
            result['success'] = 1
        except:
            result['success'] = 0

        self.response.cache_control = 'public'
        self.response.cache_control.max_age = 21600 #6 hours
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(json.dumps(result, indent=4))


class SearchHandler(webapp2.RequestHandler):
    def get(self):
        query = self.request.get('query')
        result = {}

        try:
            songs = parseSearch(query)
            result['songs'] = songs
            result['success'] = 1
        except:
            result['success'] = 0

        self.response.cache_control = 'public'
        self.response.cache_control.max_age = 21600 #6 hours
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(json.dumps(result, indent=4))

app = webapp2.WSGIApplication(
        [
            ('/', MainHandler),
            ('/home', HomeHandler),
            ('/artist', ArtistHandler),
            ('/search', SearchHandler)
        ], debug=True)
