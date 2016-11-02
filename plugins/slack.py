# -*- coding: utf-8 -*-
import os

import requests
from slackbot.bot import respond_to, listen_to

#from ..slackbot_settings import API_TOKEN
from .apis.vision import detect_text, get_required_entities
from .apis.language import analyze_entities
from .apis.kintone import create_card


@respond_to('こんにちは')
@respond_to('今日は')
def hello(message):
    message.reply('こんにちは!')


def download_image(url):
    token = os.environ.get('SLACK_API_KEY')
    resp = requests.get(url, headers={'Authorization': "Bearer " + token})
    if resp.ok:
        path = os.path.join(os.path.dirname(__file__), "./downloaded.png")
        with open(path, "wb") as f:
            f.write(resp.content)
            return path


@listen_to('(.*)')
def anyone(message, something):
    if 'file' in message.body:
        url = message.body['file']['url_private_download']
        path = download_image(url)
        text = detect_text(path)
        entities = analyze_entities(text)
        import pprint
        pprint.pprint(entities)
        entities = get_required_entities(entities)
        print(entities)
        create_card(entities, path)
        message.reply('名刺情報を登録しました。')
    else:
        message.reply('私はねこが好きです。')
