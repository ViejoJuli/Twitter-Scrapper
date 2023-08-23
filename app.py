import base64
import hashlib
from os import environ as env
from dotenv import load_dotenv
import re
import requests
import tweepy

from requests_oauthlib import OAuth2Session
from flask import Flask, request, redirect, session, url_for, render_template

load_dotenv()

print('API_KEY:  {}'.format(env['API_KEY']))
print('HOSTNAME: {}'.format(env['HOSTNAME']))
print('PORT:     {}'.format(env['PORT']))

# app = Flask(__name__)
# app.secret_key = os.urandom(50)
