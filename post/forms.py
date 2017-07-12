# -*- coding: utf-8 -*-
from django import forms

class LoginForm(forms.Form):
	username = forms.CharField(label="پست الکترونیک")
	password = forms.CharField(widget=forms.PasswordInput() , label="کلمه عبور")