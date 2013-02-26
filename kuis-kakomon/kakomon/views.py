# -*- coding: utf-8 -*-
"""
kakomon.views
"""

"""
import logging

from google.appengine.api import users
from google.appengine.api import memcache
from werkzeug import (
  unescape, redirect, Response,
)
from werkzeug.exceptions import (
  NotFound, MethodNotAllowed, BadRequest
)

from kay.utils import (
  render_to_response, reverse,
  get_by_key_name_or_404, get_by_id_or_404,
  to_utc, to_local_timezone, url_for, raise_on_dev
)
from kay.i18n import gettext as _
from kay.auth.decorators import login_required

"""

from werkzeug import redirect, Response
from kay.utils import (render_to_response, url_for)

from kakomon.models import (Lecture, Kakomon)
from kakomon.forms import (PasswordForm, AddForm, UploadForm, CommentForm, DeleteForm)

def index(request):
  '''
  Lecture(id=1,name='A',grade=2,semester=1,comment='hogehoge').put()
  Lecture(id=2,name='B',grade=2,semester=1,comment='hogehoge').put()
  Lecture(id=3,name='C',grade=2,semester=1,comment='hogehoge').put()
  Lecture(id=4,name='D',grade=2,semester=2,comment='hogehoge').put()
  Lecture(id=5,name='E',grade=2,semester=2,comment='hogehoge').put()
  Lecture(id=6,name='F',grade=3,semester=1,comment='hogehoge').put()
  Lecture(id=7,name='G',grade=3,semester=1,comment='hogehoge').put()
  '''
  return render_to_response('kakomon/index.html')

def lectures(request, grade):
  kakomons_dict = {}
  year_list = [2008, 2009, 2010, 2011, 2012, 2013, 2014]
  lectures = Lecture.all().filter('grade =', grade)
  for lecture in lectures:
    kakomons_dict[lecture.id] = []
    for year in year_list:
      if Kakomon.all().filter('lecture =', lecture).filter('year =', year).get():
        kakomons_dict[lecture.id].append(Kakomon.all().filter('lecture =', lecture).filter('year =', year))
    #kakomons_dict[lecture.id] = Kakomon.all().filter('lecture =', lecture)
  return render_to_response('kakomon/lectures.html',
                            {'grade'   : grade,
                             'lectures': lectures,
                             'kakomons_dict': kakomons_dict,
                             'year_list': year_list})

def download(request, id, name, year, ext):
  lecture = Lecture.all().filter('id =', id).get()
  kakomon = Kakomon.all().filter('lecture =', lecture).filter('year =', year).get()
  return Response(mimetype=kakomon.mimetype, response=kakomon.file)

def authorize(request):
  form = PasswordForm()
  if request.method == "POST" and form.validate(request.form):
    if form['password'] == 'you_are_beautiful':
      return redirect(url_for('kakomon/manage'))
  return render_to_response('kakomon/authorize.html',
                            {'form'  : form.as_widget(),
                             'method': request.method})

def manage(request):
  lectures = []
  for i in range(1, 5):
    lectures.append(Lecture.all().filter('grade =', i))
  return render_to_response('kakomon/manage.html',
                            {'lectures': lectures})

def manage_lectures(request, id):
  lecture = Lecture.all().filter('id =', id).get()
  edit_flag = ''

  upload_form = UploadForm()
  comment_form = CommentForm({'comment': lecture.comment})
  delete_form = DeleteForm()

  if request.method == "POST" and upload_form.validate(request.form, request.files):
    edit_flag = 'upload'
    kakomon = Kakomon.all().filter('lecture =', lecture).filter('year =', upload_form['year']).get()
    if kakomon: kakomon.delete()
    mimetype = request.files['file'].content_type
    ext = request.files['file'].filename.split('.')[1]
    Kakomon(lecture=lecture, year=upload_form['year'], teacher=upload_form['teacher'],
            file=upload_form['file'], mimetype=mimetype, ext=ext).put()

  elif request.method == "POST" and delete_form.validate(request.form) and delete_form['years']:
    edit_flag = 'delete'
    for year in delete_form['years']:
      kakomons = Kakomon.all().filter('lecture =', lecture)
      kakomons.filter('year =', year).get().delete()

  elif request.method == "POST" and comment_form.validate(request.form):
    edit_flag = 'comment'
    lecture.comment = comment_form['comment'].replace('\r\n', '\n').replace('\n', '<br/>')
    lecture.put()

  elif request.method == "POST":
    lecture.delete()
    return redirect(url_for('kakomon/manage'))
  years = []
  for kakomon in Kakomon.all().filter('lecture =', lecture).order('year'):
    years.append(kakomon.year)
  delete_form.years.choices = years

  return render_to_response('kakomon/manage_lecture.html',
                            {'file_form': upload_form.as_widget(),
                             'comment_form': comment_form.as_widget(),
                             'delete_form': delete_form.as_widget(),
                             'lecture': lecture,
                             'years': years,
                             'flag': edit_flag})

def add_lectures(request):
  add_form = AddForm()
  if request.method == "POST" and add_form.validate(request.form):
    Lecture(id=add_form['id'], name=add_form['name'], grade=add_form['grade'],
            comment=add_form['comment'] ).put()
    return redirect(url_for('kakomon/manage'))
  return render_to_response('kakomon/add_lectures.html',
                            {'add_form': add_form.as_widget()})
