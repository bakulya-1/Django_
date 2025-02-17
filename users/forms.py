from django import forms



class RegisterForm(forms.Form):
    username = forms.CharField(required=True)
    email = forms.EmailField()
    password = forms.CharField(min_length=3)
    password_confirm = forms.CharField(min_length=3)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password_confirm")
        if (password and password_confirm) and (password != password_confirm):
            raise forms.ValidationError(message="passwords do not match!")
        return cleaned_data




class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(min_length=3, widget=forms.PasswordInput)


