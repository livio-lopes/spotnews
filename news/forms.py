from django import forms
from news.models import User, Category

# from datetime import datetime


class CreateCategoriesModelForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].label = "Nome"
        self.fields["name"].required = True
        self.fields["name"].max_length = 200

    # name = forms.CharField(max_length=200, required=True, label="Nome")


class CreateNewsForm(forms.Form):
    pass
