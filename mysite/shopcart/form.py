from django import forms
from django.contrib.auth.models import User


class RegisterCreditCardForm(forms.Form):
    number = forms.CharField(required=True)
    date = forms.DateTimeField(required=True)
    name =forms.CharField(required=True)
    safety_key = forms.CharField(required=True)


    def is_valid(self):

            valid = True

            if not super(RegisterCreditCardForm, self).is_valid():
                self.add_error('Please, verify data')
                valid = False

            return valid

    def add_error(self, message):
            errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
            errors.append(message)