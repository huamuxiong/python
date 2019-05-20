from django import forms
from .models import UserAdvice
import re

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = UserAdvice
        fields = ['nickname', 'email', 'advices', 'userA']

    def clean_email(self):
        email = self.cleaned_data['email']
        REGEX_EMAIL = "^[a-z0-9A-Z]+[- | a-z0-9A-Z . _]+@([a-z0-9A-Z]+(-[a-z0-9A-Z]+)?\\.)+[a-z]{2,}$"
        p = re.compile(REGEX_EMAIL)
        if p.match(email):
            return email
        else:
            raise forms.ValidationError('邮箱格式不正确', code='email_invalid')
