# -*- coding: utf-8 -*-
import pykintone
from pykintone import model
import pykintone.structure_field as sf


class BusinessCard(model.kintoneModel):

    def __init__(self, app, name, company, location, impression, submitter, image_path):
        super(BusinessCard, self).__init__()
        self.name = name
        self.company = company
        self.location = location
        self.impression = impression
        self.submitter = submitter
        self.image = [sf.File.upload(image_path, app)]


def create_card(comment, entities, file_path, submitter, conf_path):
    app = pykintone.load(conf_path).app()

    name, company, location = entities['PERSON'], entities['ORGANIZATION'], entities['LOCATION']
    card = BusinessCard(app, name, company, location, comment, submitter, file_path)
    result = app.create(card)

    if result.ok:
        return result
    else:
        print(result.error)
