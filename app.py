import tweepy
import configparser

config = configparser.ConfigParser()

config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

# Authenticate
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()

print(public_tweets)

# # print('API_KEY:  {}'.format(env['API_KEY']))
# # print('HOSTNAME: {}'.format(env['HOSTNAME']))
# # print('PORT:     {}'.format(env['PORT']))

# # app = Flask(__name__)
# # app.secret_key = os.urandom(50)
# client_id = env['CLIENT_ID']
# client_secret = env['CLIENT_SECRET']
# print(client_id)
