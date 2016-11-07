# -*- coding: utf-8 -*-
from plugins.apis.config_loader import loader

API_TOKEN = loader('plugins/config/slack.yaml')['token']

default_reply = "スイマセン。其ノ言葉ワカリマセン"

PLUGINS = [
    'plugins',
]