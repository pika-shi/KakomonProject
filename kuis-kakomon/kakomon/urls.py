# -*- coding: utf-8 -*-
# kakomon.urls
#

# Following few lines is an example urlmapping with an older interface.
"""
from werkzeug.routing import EndpointPrefix, Rule

def make_rules():
  return [
    EndpointPrefix('kakomon/', [
      Rule('/', endpoint='index'),
    ]),
  ]

all_views = {
  'kakomon/index': 'kakomon.views.index',
}
"""

from kay.routing import (
  ViewGroup, Rule
)

view_groups = [
  ViewGroup(
    Rule('/', endpoint='index', view='kakomon.views.index'),
    Rule('/lectures/<int:grade>', endpoint='lectures', view='kakomon.views.lectures'),
    Rule('/download/<int:id>/<name>_<int:year>.<ext>', endpoint='download', view='kakomon.views.download'),
    Rule('/authorize', endpoint='authorize', view='kakomon.views.authorize'),
    Rule('/manage', endpoint='manage', view='kakomon.views.manage'),
    Rule('/manage/<int:id>', endpoint='manage_lectures', view='kakomon.views.manage_lectures'),
  )
]

