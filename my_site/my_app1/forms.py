from django import forms
from django.core.exceptions import ValidationError

from .models import *


class AddPosition(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['categories'].label = "Категорія"

    class Meta:
        model = Position
        fields = ['title', 'slug_for_position', 'description', 'price', 'photo', 'published', 'categories']

    def clean_description(self):
        description = self.cleaned_data['description']
        if len(description) > 200:
            raise ValidationError('Занадто довгий опис')

        return description


class Box(forms.Form):
    class Meta:
        model = Position
        fields = '__all__'
