# -*- coding: utf-8 -*-
import argparse
import os
import sys
sys.path.append('..')

from apis.vision import detect_text
from apis.config_loader import loader


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('image_file', help='The image you\'d like to detect text.')
    args = parser.parse_args()

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    google_token = loader(os.path.join(BASE_DIR, 'config/google.yaml'))
    text = detect_text(args.image_file, google_token['token'])
    print(text)
