from django import forms
from django.forms import ModelForm

from apps.user.models import User


class UserForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['autofocus'] = True

    class Meta:
        model = User
        fields = 'first_name', 'last_name', 'telefono', 'email', 'username', 'password', 'image', 'tipo'
        exclude = ('user_permissions', 'last_login', 'date_joined', 'is_active', 'is_staff', 'groups')
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese sus nombres',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese sus apellidos',
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese su teléfono',
                }
            ),         
            'email': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese su email',
                }
            ),
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese su username',
                }
            ),
            'password': forms.PasswordInput(render_value=True,
                                            attrs={
                                                'placeholder': 'Ingrese su password',
                                            }
                                            ),

        }

    def save(self, commit=True):
        user = super().save(commit=False)
        try:
            user.set_password(self.cleaned_data['password'])
            if commit:
                user.save()
            return user
        except Exception as e:
            # Re-raise or handle as appropriate, but for now we just want it to work
            raise e


class UserProfileForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['autofocus'] = True

    class Meta:
        model = User
        fields = 'first_name', 'last_name', 'email', 'username', 'password', 'image'
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese sus nombres',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese sus apellidos',
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese su email',
                }
            ),
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese su username',
                }
            ),
            'password': forms.PasswordInput(render_value=True,
                                            attrs={
                                                'placeholder': 'Ingrese su password',
                                            }
                                            ),
        }
        exclude = ['user_permissions', 'last_login', 'date_joined', 'is_superuser', 'is_active', 'is_staff', 'groups']

    def save(self, commit=True):
        user = super().save(commit=False)
        try:
            pwd = self.cleaned_data['password']
            if user.pk:
                 # Check if password has changed (this is a simple check, ideally we use default set_password)
                 # But since we render value=True in widget, it logic might be intended to always set it.
                 # safe approach:
                 user.set_password(pwd)
            else:
                 user.set_password(pwd)
            
            if commit:
                user.save()
            return user
        except Exception as e:
             raise e
