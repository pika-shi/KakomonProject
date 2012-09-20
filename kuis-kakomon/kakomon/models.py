# -*- coding: utf-8 -*-

from google.appengine.ext import db

class Lecture(db.Model):
    id = db.IntegerProperty(required=True)
    name = db.StringProperty(required=True)
    grade = db.IntegerProperty(required=True)
    semester = db.IntegerProperty(required=True)
    comment = db.TextProperty()

class Kakomon(db.Model):
    lecture = db.ReferenceProperty(Lecture)
    year = db.IntegerProperty(required=True)
    #file = db.BlobProperty(required=True)
    file = db.StringProperty(required=True)

