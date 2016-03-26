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
		data = self.request.GET["data"]
		print "data:%s" % data 
		# result = self.getPage(data).content
		# self.response.write(result)


		# self.response.write(json.dumps(result))

		# self.response.write('get')
	def post(self):
		# def decodeUrl(url):
		# 	if url:
		# 		return urllib.unquote(url).decode('utf8') 

		
		data = self.request.get("data").decode()
		# data = ["http://www.amazon.com/s?rh=n%3A2407776011&page=1&ie=UTF8"]
		result = self.getPage(data).content
		# result = map(self.getPage, data)

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
