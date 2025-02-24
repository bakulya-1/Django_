from django import forms
from .models import Post
from  posts.models import Category, Tag


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


class SearchForm(forms.Form):
    search = forms.CharField(
        required=False,
        max_length=100,
        widget=forms.TextInput(attrs={"placeholder": "Поиск"}),
    )

    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple)

    orderings = (
        ('title', "По заголовку"),
        ("-title", "По заголовку (обратно)"),
        ("rate", "По оценке"),
        ("-rate", "По оценке (обратно)"),
        ("created_at", "По дате создания"),
        ("-created_at", "По дате создания (обратно)")
    )
    ordering = forms.ChoiceField(choices=orderings, widget=forms.Select(attrs={
        "class": "form-control"
    }))


class PostUpdateForm(forms.ModelForm):
    class Mets:
        model = Post
        fields = ["title", "content", "image", "rate"]






