# -*- coding: utf-8 -*-
# kakomon.models

from google.appengine.ext import db

class Lecture(db.Model):
    id = db.IntegerProperty(required=True)
    name = db.StringProperty(required=True)
    grade = db.IntegerProperty(required=True)
    semester = db.IntegerProperty(required=True)

class Kakomon(db.Model):
    #id = db.ReferenceProperty(Lecture)
    #year = db.IntegerProperty(required=True)
    tmp = db.IntegerProperty()
    file = db.BlobProperty(required=True)

#class Comment(db.Model):
#      user = db.StringProperty()
#      body = db.TextProperty(required=True)
#      created = db.DateTimeProperty(auto_now_add=True)
