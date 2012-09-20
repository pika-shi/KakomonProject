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

from kakomon.models import Lecture, Kakomon
from kakomon.forms import (UploadForm, PasswordForm)

# Create your views here.

def index(request):
  '''
  form = UploadForm()
  if request.method == "POST" and form.validate(request.form, request.files):
    kakomon = Kakomon(file=form['upload_file'])
    kakomon.tmp = 1
    kakomon.put()
    return Response(mimetype=request.files['upload_file'].content_type, response=form['upload_file'])
    #return redirect(url_for('kakomon/index'))
  k_file = Kakomon.all().fetch(1)
  return render_to_response('kakomon/index.html',
                            {'form': form.as_widget(),
                             'k_file': k_file})
  '''
  '''
  Lecture(id=1,name='A',grade=2,semester=1,comment='hogehoge').put()
  Lecture(id=2,name='B',grade=2,semester=1,comment='hogehoge').put()
  Lecture(id=3,name='C',grade=2,semester=1,comment='hogehoge').put()
  Lecture(id=4,name='D',grade=2,semester=2,comment='hogehoge').put()
  Lecture(id=5,name='E',grade=2,semester=2,comment='hogehoge').put()
  Lecture(id=6,name='F',grade=3,semester=1,comment='hogehoge').put()
  Lecture(id=7,name='G',grade=3,semester=1,comment='hogehoge').put()

  Kakomon(lecture=Lecture.all().filter('id =', 1).get(),year=2010,file='hogehoge').put()
  Kakomon(lecture=Lecture.all().filter('id =', 1).get(),year=2011,file='hogehoge').put()
  Kakomon(lecture=Lecture.all().filter('id =', 2).get(),year=2010,file='hogehoge').put()
  Kakomon(lecture=Lecture.all().filter('id =', 2).get(),year=2011,file='hogehoge').put()
  Kakomon(lecture=Lecture.all().filter('id =', 3).get(),year=2010,file='hogehoge').put()
  Kakomon(lecture=Lecture.all().filter('id =', 3).get(),year=2011,file='hogehoge').put()
  Kakomon(lecture=Lecture.all().filter('id =', 4).get(),year=2010,file='hogehoge').put()
  Kakomon(lecture=Lecture.all().filter('id =', 4).get(),year=2011,file='hogehoge').put()
  Kakomon(lecture=Lecture.all().filter('id =', 5).get(),year=2010,file='hogehoge').put()
  Kakomon(lecture=Lecture.all().filter('id =', 5).get(),year=2011,file='hogehoge').put()
  Kakomon(lecture=Lecture.all().filter('id =', 6).get(),year=2010,file='hogehoge').put()
  Kakomon(lecture=Lecture.all().filter('id =', 6).get(),year=2011,file='hogehoge').put()
  Kakomon(lecture=Lecture.all().filter('id =', 7).get(),year=2010,file='hogehoge').put()
  Kakomon(lecture=Lecture.all().filter('id =', 7).get(),year=2011,file='hogehoge').put()
  '''
  return render_to_response('kakomon/index.html')

def lectures(request, grade):
  kakomons_dict = {}
  lectures = Lecture.all().filter('grade =', grade)
  for lecture in lectures:
    kakomons_dict[lecture.id] = Kakomon.all().filter('lecture =', lecture)
  return render_to_response('kakomon/lectures.html',
                            {'grade'   : grade,
                             'lectures': lectures,
                             'kakomons_dict': kakomons_dict})

def download(request, name, year):
  pass

def authorize(request):
  form = PasswordForm()
  if request.method == "POST" and form.validate(request.form):
    if form['password'] == 'pika_shi':
      return redirect(url_for('kakomon/manage'))
  return render_to_response('kakomon/authorize.html',
                            {'form'  : form.as_widget(),
                             'method': request.method})

def manage(request):
  lectures = Lecture.all()
  return render_to_response('kakomon/manage.html',
                            {'lectures': lectures})

def manage_lectures(request, id):
  return render_to_response('kakomon/manage_lecture.html',
                            {'id': id})
