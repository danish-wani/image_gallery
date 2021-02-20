from django.db import models
from .helpers import get_or_create_category_directory_path
from django.db.models.signals import post_delete
from .signals import delete_media_image
from django.utils.translation import gettext_lazy as _


class ImageCategory(models.TextChoices):
    """
        Category Choices
    """
    WILDLIFE = 'wildlife', _('Wildlife')
    LANDSCAPE = 'landscape', _('Landscape')
    PORTRAIT = 'portrait', _('Portrait')
    AERIAL = 'aerial', _('Aerial')
    SPORTS = 'sports', _('Sports')
    OTHER = 'other', _('Other')


class Gallery(models.Model):
    """
        Image Gallery
    """

    added_on = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=20, choices=ImageCategory.choices)
    image = models.ImageField(upload_to=get_or_create_category_directory_path)

    class Meta:
        db_table = 'Gallery'
        ordering = ('-added_on', )

    def __str__(self):
        """

        """
        return str(self.image.name) + ' | ' + str(self.get_category_display())


# Post delete signal to delete image file of the deleted instance from media

post_delete.connect(delete_media_image, sender=Gallery)
