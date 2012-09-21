# -*- coding: utf-8 -*-

from kay.utils import forms

class UploadForm(forms.Form):
      year = forms.ChoiceField(choices=[2010, 2011, 2012], required=True)
      file = forms.FileField(required=True)

class PasswordForm(forms.Form):
      password = forms.TextField(required=True, widget=forms.PasswordInput)
