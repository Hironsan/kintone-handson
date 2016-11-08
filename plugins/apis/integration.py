# -*- coding: utf-8 -*-
from .language import extract_required_entities
from .vision import detect_text


def extract_entities_from_img(img_path, access_token):

    text = detect_text(img_path, access_token)
    entities = extract_required_entities(text, access_token)

    return entities
