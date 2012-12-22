# -*- coding: utf-8 -*-

from kay.utils import forms
from datetime import datetime

year_list = []
for i in range(2008, datetime.now().year + 1):
      year_list.append(i)

class PasswordForm(forms.Form):
      password = forms.TextField(required=True, label='パスワード'.decode('utf-8'), widget=forms.PasswordInput)

class AddForm(forms.Form):
      id = forms.NumberField(required=True, label='講義番号'.decode('utf-8'))
      name = forms.TextField(required=True, label='講義名'.decode('utf-8'))
      grade = forms.ChoiceField(choices=[1, 2, 3, 4], required=True, label='学年'.decode('utf-8'))
      comment = forms.TextField(required=True, label='コメント'.decode('utf-8'), widget=forms.Textarea)

class UploadForm(forms.Form):
      year = forms.ChoiceField(choices=year_list, required=True, label='年度'.decode('utf-8'))
      teacher = forms.TextField(required=True, label='担当教員'.decode('utf-8'))
      file = forms.FileField(required=True, label='ファイル'.decode('utf-8'))

class CommentForm(forms.Form):
      comment = forms.TextField(required=True, label='コメント'.decode('utf-8'), widget=forms.Textarea)

class DeleteForm(forms.Form):
      years = forms.MultiChoiceField(choices=year_list, widget=forms.CheckboxGroup)
