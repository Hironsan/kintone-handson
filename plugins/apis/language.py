# -*- coding: utf-8 -*-
import os

import requests


class Service(object):

    def __init__(self, service_name, version, feature, access_token):
        self.url = 'https://{}.googleapis.com/{}/documents:{}?key={}'.format(service_name, version, feature, access_token)

    def execute(self, body):
        header = {'Content-Type': 'application/json'}
        response = requests.post(self.url, headers=header, json=body)
        return response.json()


def analyze_entities(text):

    access_token = os.environ.get('GOOGLE_API')
    service = Service('language', 'v1beta1', 'analyzeEntities', access_token=access_token)

    body = {
        "document": {
            "type": "PLAIN_TEXT",
            "language": "JA",
            "content": text
        },
        "encodingType": "UTF8"
    }
    response = service.execute(body=body)
    return response
