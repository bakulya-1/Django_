from django import forms
from .models import Post



class PostCreateForm(forms.Form):
    image = forms.ImageField()
    title = forms.CharField(max_length=156)
    content = forms.CharField(max_length=1056)

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        content = cleaned_data.get("content")
        if (title and content) and (title.lower()==content.lower()):
            raise forms.ValidationError(message="title and content should not be same")
        return cleaned_data

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if title and title.lower() == "python":
            raise forms.ValidationError(message="python is not allowed value for title")
        return title



