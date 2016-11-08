# -*- coding: utf-8 -*-
import os

import requests
from slackbot.bot import respond_to, listen_to

from .apis.integration import extract_entities_from_img
from .apis.kintone import create_card
from .apis.config_loader import loader
BASE_DIR = os.path.dirname(__file__)


@respond_to('こんにちは')
@respond_to('今日は')
def hello(message):
    message.reply('こんにちは!')


def download_image(url, access_token=None):
    resp = requests.get(url, headers={'Authorization': "Bearer " + access_token})
    if resp.ok:
        file_name = url.split('/')[-1]
        path = os.path.join(BASE_DIR, file_name)
        with open(path, "wb") as f:
            f.write(resp.content)
            return path


@listen_to('(.*)')
def anyone(message, something):
    if 'file' in message.body:
        slack_token = loader(os.path.join(BASE_DIR, 'config/slack.yaml'))
        google_token = loader(os.path.join(BASE_DIR, 'config/google.yaml'))

        url = message.body['file']['url_private_download']
        img_path = download_image(url, slack_token['token'])

        entities = extract_entities_from_img(img_path, google_token['token'])

        comment = message.body['file']['initial_comment']['comment']
        create_card(comment, entities, img_path)
        message.reply('名刺情報を登録しました。')
    else:
        message.reply('名刺情報の登録をできますよ。')
