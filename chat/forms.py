from django import forms

from chat.models import Message


class MessageForm(forms.ModelForm):
   # new_message = forms.CharField(label='Your message:', max_length=1000)
   class Meta:
       model = Message
       # exclude = ['author', 'updated', 'created', ]
       fields = ['text']
       widgets = {
           'text': forms.TextInput(attrs={
               'id': 'message-text',
               'required': True,
               'class': 'form',
           }),
       }


class UserForm(forms.Form):
    username = forms.CharField(label = 'Username', max_length = 1024)
    password = forms.CharField(widget=forms.PasswordInput(),label='Password',max_length=1024)

class SignUpForm(forms.Form):
    username = forms.CharField(label = 'Username', max_length = 1024)
    password = forms.CharField(widget=forms.PasswordInput(),label='Password',max_length=1024)
    email = forms.EmailField(label='Email')
    fname = forms.CharField(label='First Name',max_length = 1024)
    sname = forms.CharField(label='Second Name',max_length = 1024)

class AddFriendForm(forms.Form):
    username = forms.CharField(label='', max_length=150, required=False,  widget=forms.TextInput(attrs={'class': 'special'}))
