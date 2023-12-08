from django import forms
from news.models import Category, News, User

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


class CreateNewsModelForm(forms.ModelForm):
    class Meta:
        model = News
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].label = 'Título'
        self.fields['title'].widget = forms.TextInput(
            attrs={'type': 'text', 'name': 'title', 'maxlength': '200'}
        )
        self.fields['content'].label = 'Conteúdo'
        self.fields['content'].widget = forms.Textarea(
            attrs={'type': 'text', 'name': 'content'}
        )
        self.fields['author'].label = 'Autoria'
        self.fields['author'].widget = forms.Select(
            attrs={'type': 'text', 'name': 'author'},
            choices=[(user.id, user.name) for user in User.objects.all()]
        )
        self.fields['created_at'].label = 'Criado em'
        self.fields['created_at'].widget = forms.DateInput(
            attrs={'type': 'date', 'name': 'created_at',}
        )
        self.fields['image'].label = 'URL da Imagem'
        self.fields['image'].widget = forms.FileInput(
            attrs={'type': 'file', 'name': 'image'}
        )

        self.fields['categories'] = forms.ModelMultipleChoiceField(
            label='categories',
            queryset=Category.objects.all(),
            widget=forms.CheckboxSelectMultiple,
            required=True,
        )
