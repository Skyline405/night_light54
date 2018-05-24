from django.template.defaulttags import register


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


@register.filter
def do_range(end, start, step=1):
    return range(start, end+1, step)
