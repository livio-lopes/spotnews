from django import forms


class CreatCategoriesForm(forms.Form):
    name = forms.CharField(
        max_length=200,
        required=True,
        label="Nome"
    )
