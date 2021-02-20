from enum import Enum


class Category(Enum):
    WILDLIFE = 'wildlife', 'Wildlife'
    LANDSCAPE = 'landscape', 'Landscape'
    PORTRAIT = 'portrait', 'Portrait'
    AERIAL = 'aerial', 'Aerial'
    SPORTS = 'sports', 'Sports'


CATEGORY_CHOICES = (
    Category.WILDLIFE.value,
    Category.LANDSCAPE.value,
    Category.PORTRAIT.value,
    Category.AERIAL.value,
    Category.SPORTS.value
)
