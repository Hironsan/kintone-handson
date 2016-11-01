# -*- coding: utf-8 -*-
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

app = pykintone.load("./config.yaml").app()
myfiles = ["/Users/smap4/Python/Kintone/image.png"]

card = BusinessCard()
card.name = 'Hironsan'
card.company = ''
card.location = '東京'
card.files = [sf.File.upload(f, app) for f in myfiles]
print(card.files)

result = app.create(card)
