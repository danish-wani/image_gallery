# __author__ = 'danish-wani'


from pathlib import Path
from django.conf import settings


def get_or_create_category_directory_path(instance, filename):
    """
        Returns a category based media path
    """
    category = instance.category
    category = category.lower()
    category_path = Path.joinpath(settings.MEDIA_ROOT, category)

    if not category_path.exists():
        Path.mkdir(category_path)

    return category + '/' + filename
