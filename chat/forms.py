from django import forms

class MessageForm(forms.Form):
    new_message = forms.CharField(label='Your message:', max_length=1000)