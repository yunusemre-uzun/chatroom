from django import forms

class MessageForm(forms.Form):
    new_message = forms.CharField(label='Your message:', max_length=1000)

class UserForm(forms.Form):
    username = forms.CharField(label = 'Username', max_length = 1024)
