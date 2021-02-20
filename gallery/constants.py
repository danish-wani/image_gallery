from enum import Enum


class Category(Enum):
    WILDLIFE = 'wildlife'
    LANDSCAPE = 'landscape'
    PORTRAIT = 'portrait'
    AERIAL = 'aerial'
    SPORTS = 'sports'


CATEGORY_CHOICES = (
    (Category.WILDLIFE.value, Category.WILDLIFE.name),
    (Category.LANDSCAPE.value, Category.LANDSCAPE.name),
    (Category.PORTRAIT.value, Category.PORTRAIT.name),
    (Category.AERIAL.value, Category.AERIAL.name),
    (Category.SPORTS.value, Category.SPORTS.name),
)
