from django import forms

class MessageForm(forms.Form):
    new_message = forms.CharField(label='Your message:', max_length=1000)

class UserForm(forms.Form):
    username = forms.CharField(label = 'Username ', max_length = 1024)
    password = forms.CharField(widget=forms.PasswordInput(),label='Password',max_length=1024)

class SignUpForm(forms.Form):
    username = forms.CharField(label = 'Username ', max_length = 1024)
    password = forms.CharField(widget=forms.PasswordInput(),label='Password ',max_length=1024)
    email = forms.EmailField(label='Email ')
    fname = forms.CharField(label='First Name ',max_length = 1024)
    sname = forms.CharField(label='Second Name ',max_length = 1024)

class AddFriendForm(forms.Form):
    username = forms.CharField(label="Username ",max_length=150,required=False)
