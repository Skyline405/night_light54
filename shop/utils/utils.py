import uuid
from django.conf import settings
from django.utils.safestring import mark_safe


def make_upload_path(instance, filename, prefix=False):
    f_hash = str(uuid.uuid1())
    parts = filename.split('.')
    name = parts[0]
    ext = parts[-1]
    new_name = name + '.' + f_hash + '.' + ext
    return u"%s/%s" % (settings.PRODUCTS_IMG_DIR, new_name)


def get_img_markup(image, size=32):
    if not image:
        return '-'
    return mark_safe('<img src="%s" height="%s" />' % (image.url, size))
