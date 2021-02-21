# __author__ = 'danish-wani'


from django import forms
from .models import ImageCategory, Gallery


class GalleryForm(forms.ModelForm):
    """
        Gallery form for adding Images to gallery along with their category
    """

    category = forms.ChoiceField(choices=ImageCategory.choices)

    def __init__(self, *args, **kwargs):
        super(GalleryForm, self).__init__()

        self.fields['category'].widget.attrs['class'] = "form-control form-select form-select-sm mb-3"
        self.fields['image'].widget.attrs['class'] = "form-control"

    class Meta:
        model = Gallery
        fields = '__all__'
