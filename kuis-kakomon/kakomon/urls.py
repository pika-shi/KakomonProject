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
  )
]

