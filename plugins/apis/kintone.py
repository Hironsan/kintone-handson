# -*- coding: utf-8 -*-
import os

import pykintone
from pykintone import model
import pykintone.structure_field as sf


class BusinessCard(model.kintoneModel):

    def __init__(self, app, name, company, location, impression, image_path):
        super(BusinessCard, self).__init__()
        self.name = name
        self.company = company
        self.location = location
        self.impression = impression
        self.image = [sf.File.upload(image_path, app)]


def create_card(comment, entities, file_path):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    conf_path = os.path.join(base_dir, 'config/kintone.yaml')
    app = pykintone.load(conf_path).app()

    name, company, location = entities['PERSON'], entities['ORGANIZATION'], entities['LOCATION']
    card = BusinessCard(app, name, company, location, comment, file_path)
    result = app.create(card)

    return result
