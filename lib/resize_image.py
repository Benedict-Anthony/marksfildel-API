from PIL import Image, ImageOps
import io
from django.core.files import File


def resize_image(image):
    size = (350, 350)
    img = Image.open(image)
    img.convert("RGB")
    img.thumbnail(size)
    thumb_io = io.BytesIO()
    img.save(thumb_io, "PNG", quality=95)
    thumbnail = File(thumb_io, name=image.name)
    return thumbnail
