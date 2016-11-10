# -*- coding: utf-8 -*-
import argparse
import os
import sys
sys.path.append('..')

from apis.language import extract_required_entities
from apis.config_loader import loader


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('text_file', help='The text you\'d like to extract entities.')
    args = parser.parse_args()

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    google_token = loader(os.path.join(BASE_DIR, 'config/google.yaml'))
    text = open(args.text_file, encoding="utf-8").read()
    entities = extract_required_entities(text, google_token['token'])
    print(entities)
