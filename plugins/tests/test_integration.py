# -*- coding: utf-8 -*-
import argparse
import os
import sys
sys.path.append('..')

from apis.integration import extract_entities_from_img
from apis.config_loader import loader


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('image_file', help='The image you\'d like to extract entities.')
    args = parser.parse_args()

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    google_token = loader(os.path.join(BASE_DIR, 'config/google.yaml'))
    entities = extract_entities_from_img(args.image_file, google_token['token'])
    print(entities)
