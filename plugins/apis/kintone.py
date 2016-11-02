# -*- coding: utf-8 -*-
import os

import pykintone
from pykintone import model
import pykintone.structure_field as sf


class BusinessCard(model.kintoneModel):

    def __init__(self):
        super(BusinessCard, self).__init__()
        self.name = ''
        self.company = ''
        self.location = ''
        self.files = [sf.File()]


def create_card(entities, file_path):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    conf_path = os.path.join(base_dir, 'config/kintone.yaml')
    app = pykintone.load(conf_path).app()

    card = BusinessCard()
    card.name = entities.get('PERSON', '')
    card.company = entities.get('ORGANIZATION', '')
    card.location = entities.get('LOCATION', '')
    card.files = [sf.File.upload(f, app) for f in [file_path]]
    result = app.create(card)

    return result
