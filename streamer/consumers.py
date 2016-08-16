from channels import Group
from channels.sessions import channel_session
from .models import *

@channel_session
def ws_connect(message):
	keyword = message['message']

	print keyword
	# cred_path = os.path.join(os.path.dirname(__file__), "static/app-creds.txt")
	# cred = open(cred_path, 'r')
	# app_key = cred.readline().rstrip()
	# app_secret = cred.readline().rstrip()
	# access_token = cred.readline().rstrip()
	# access_token_secret = cred.readline().rstrip()
	# cred.close()
	
	# auth = tweepy.OAuthHandler(app_key, app_secret)
	# auth.set_access_token(access_token, access_token_secret)
	# l = StdOutListener()
	# stream = tweepy.Stream(auth, l)
	# stream.filter(track=keyword, async=True)

	Group('streamer-' + keyword).add(message.reply_channel)
	message.channel_session['keyword'] = keyword

@channel_session
def ws_receive(message):
    label = message.channel_session['room']
    room = Room.objects.get(label=label)
    data = json.loads(message['text'])
    m = room.messages.create(handle=data['handle'], message=data['message'])
    Group('chat-'+label).send({'text': json.dumps(m.as_dict())})

class StdOutListener(tweepy.StreamListener):
	
	def on_data(self, data):
		# print(data)
		j = json.loads(data)
		print(j['text'])
		return True

	def on_error(self, status):
		print (status)