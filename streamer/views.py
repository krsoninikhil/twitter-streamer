from django.shortcuts import render
import tweepy

def index(request):
	return render(request, 'index.html', {})

def get_tweets(request):
	keyword = [request.GET['key']]

	cred_path = os.path.join(os.path.dirname(__file__), "static/app-creds.txt")
	cred = open(cred_path, 'r')
	app_key = cred.readline().rstrip()
	app_secret = cred.readline().rstrip()
	access_token = cred.readline().rstrip()
	access_token_secret = cred.readline().rstrip()
	cred.close()
	
	auth = tweepy.OAuthHandler(app_key, app_secret)
	auth.set_access_token(access_token, access_token_secret)
	l = StdOutListener()
	stream = tweepy.Stream(auth, l)
	stream.filter(track=keyword, async=True)


class StdOutListener(tweepy.StreamListener):
	
	def on_data(self, data):
		# print(data)
		j = json.loads(data)
		print(j['text'])		
		return True

	def on_error(self, status):
		print (status)