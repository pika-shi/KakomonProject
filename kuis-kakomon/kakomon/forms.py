# -*- coding: utf-8 -*-

from kay.utils import forms

class UploadForm(forms.Form):
      year = forms.ChoiceField(choices=[2008, 2009, 2010, 2011, 2012, 2013, 2014], required=True)
      file = forms.FileField(required=True)

class PasswordForm(forms.Form):
      password = forms.TextField(required=True, label='パスワード'.decode('utf-8'), widget=forms.PasswordInput)
