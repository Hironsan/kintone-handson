# -*- coding: utf-8 -*-
import os

import requests
from slackbot.bot import respond_to, listen_to

from ..slackbot_settings import API_TOKEN


@respond_to('こんにちは')
@respond_to('今日は')
def hello(message):
    message.reply('こんにちは!')


def download_image(url):
    #token = os.environ.get('SLACK_API_KEY')
    resp = requests.get(url, headers={'Authorization': "Bearer " + API_TOKEN})
    if resp.ok:
        path = os.path.join(os.path.dirname(__file__), "./downloaded.png")
        with open(path, "wb") as f:
            f.write(resp.content)


def download_image(url):
    resp = requests.get(url, headers={'Authorization': "Bearer " + API_TOKEN})
    return resp.content if resp.ok else ''


@listen_to('(.*)')
def anyone(message):
    if 'file' in message.body:
        url = message.body['file']['url_private_download']
        download_image(url)
    message.reply('猫')
