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

from kakomon.models import Kakomon
from kakomon.forms import UploadForm

# Create your views here.

def index(request):
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

def lectures(request, grade):
  pass

def upload(request):
  pass
