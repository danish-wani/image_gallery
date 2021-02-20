from django import forms
from .models import ImageCategory, Gallery


class GalleryForm(forms.ModelForm):
    """
        Gallery form for adding Images to gallery along with their category
    """

    category = forms.ChoiceField(choices=ImageCategory.choices)

    class Meta:
        model = Gallery
        fields = '__all__'
