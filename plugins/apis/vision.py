# -*- coding: utf-8 -*-
import base64
import os

import requests


class Service(object):

    def __init__(self, service_name, version, access_token):
        self.url = 'https://{}.googleapis.com/{}/images:annotate?key={}'.format(service_name, version, access_token)

    def execute(self, body):
        header = {'Content-Type': 'application/json'}
        response = requests.post(self.url, headers=header, json=body)
        return response.json()


def encode_image(image):
    image_content = image.read()
    return base64.b64encode(image_content).decode()


def get_required_entities(entities):
    res = {'ORGANIZATION': '', 'PERSON': '', 'LOCATION': ''}
    for entity in entities['entities']:
        t = entity['type']
        if t in res:
            res[t] += entity['name']

    return res


def detect_text(photo_file):
    """
    Run a text detection request on a single image
    """

    access_token = os.environ.get('GOOGLE_API')
    service = Service('vision', 'v1', access_token=access_token)

    with open(photo_file, 'rb') as image:
        base64_image = encode_image(image)
        body = {
            'requests': [{
                'image': {
                    'content': base64_image,
                },
                'features': [{
                    'type': 'TEXT_DETECTION',
                    'maxResults': 1,
                }]

            }]
        }
        response = service.execute(body=body)
        text = response['responses'][0]['textAnnotations'][0]['description']
        print('Found text: {}'.format(text))
        return text
