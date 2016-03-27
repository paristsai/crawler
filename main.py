import webapp2
from google.appengine.api import urlfetch
import json
import urllib

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World!!!')


class UrlHandler(webapp2.RequestHandler):
	def get(self):
		data = self.request.GET["data"].decode()
		print "data:%s" % data
		result = self.getPage(data).content
		self.response.write(result)

	def post(self):
		data = self.request.get("data").decode()
		result = self.getPage(data).content
		self.response.write(result)

	def getPage(self, url):
		if isinstance(url, basestring):
			return urlfetch.fetch(url)
		elif isinstance(url, list):
			return map(urlfetch.fetch, url)

app = webapp2.WSGIApplication([
    (r'/', MainPage),
    (r'/proxy', UrlHandler),
], debug=True)

#update: $ gcloud preview app deploy app.yaml
