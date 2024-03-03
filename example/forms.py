from django import forms

from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox, ReCaptchaV2Invisible, ReCaptchaV3

class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    captcha = ReCaptchaField(widget=ReCaptchaV3)