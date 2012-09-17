# -*- coding: utf-8 -*-

from kay.utils import forms

class UploadForm(forms.Form):
      upload_file = forms.FileField(required=True)
