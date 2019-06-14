from django.forms import Form, CharField, PasswordInput


class LoginForm(Form):
    username = CharField(label="Username", max_length=64)
    password = CharField(label="Password", widget=PasswordInput())