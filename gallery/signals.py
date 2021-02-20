from pathlib import Path


def delete_media_image(sender, instance, **kwargs):
    """
        Remove image file of deleted instance from media
    """
    image_path = Path(instance.image.path)
    if image_path.exists():
        Path.unlink(image_path)
