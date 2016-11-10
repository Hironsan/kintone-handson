# -*- coding: utf-8 -*-
import argparse
import os
import sys
sys.path.append('..')

from apis.kintone import create_card


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('image_file', help='The image you\'d like to detect text.')
    args = parser.parse_args()

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    kintone_conf = os.path.join(BASE_DIR, 'config/kintone.yaml')
    comment = 'First Impression'
    submitter = '砂糖ひろし'
    entities = {'PERSON': '山田太郎', 'LOCATION': '東京都', 'ORGANIZATION': 'XXX株式会社'}
    create_card(comment, entities, args.image_file, submitter, kintone_conf)
