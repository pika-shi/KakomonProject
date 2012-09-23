# -*- coding: utf-8 -*-

from kay.utils import forms

class PasswordForm(forms.Form):
      password = forms.TextField(required=True, label='パスワード'.decode('utf-8'), widget=forms.PasswordInput)

class UploadForm(forms.Form):
      year = forms.ChoiceField(choices=[2008, 2009, 2010, 2011, 2012, 2013, 2014], required=True, label='年度'.decode('utf-8'))
      file = forms.FileField(required=True, label='ファイル'.decode('utf-8'))

class CommentForm(forms.Form):
      comment = forms.TextField(required=True, label='コメント'.decode('utf-8'), widget=forms.Textarea)

class DeleteForm(forms.Form):
      choices = forms.MultiChoiceField(choices=[1, 2, 3])
