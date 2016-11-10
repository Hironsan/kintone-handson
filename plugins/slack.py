# -*- coding: utf-8 -*-
import os

import requests
from slackbot.bot import respond_to, listen_to

from .apis.integration import extract_entities_from_img
from .apis.kintone import create_card
from .apis.config_loader import loader
BASE_DIR = os.path.dirname(__file__)


def download_image(url, access_token=None):
    resp = requests.get(url, headers={'Authorization': "Bearer " + access_token})
    if resp.ok:
        file_name = url.split('/')[-1]
        path = os.path.join(BASE_DIR, file_name)
        with open(path, "wb") as f:
            f.write(resp.content)
            return path


def get_user_name(user, token):
    url = 'https://slack.com/api/users.info?token={}&user={}'.format(token, user)
    response = requests.get(url).json()
    if response['ok']:
        return response['user']['name']
    else:
        return ''


# Write your code