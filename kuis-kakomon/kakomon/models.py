# -*- coding: utf-8 -*-
# kakomon.models

from google.appengine.ext import db

class Lecture(db.Model):
    id = db.IntegerProperty(required=True)
    name = db.StringProperty(required=True)

class Kakomon(db.Model):
    id = db.ReferenceProperty(Lecture)
    year = db.IntegerProperty(required=True)
    file = db.BlobProperty(required=True)
