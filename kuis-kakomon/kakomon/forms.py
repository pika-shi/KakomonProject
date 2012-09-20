# -*- coding: utf-8 -*-

from kay.utils import forms

class UploadForm(forms.Form):
      upload_file = forms.FileField(required=True)

class PasswordForm(forms.Form):
      password = forms.TextField(required=True, widget=forms.PasswordInput)
