from django import template

register = template.Library()


@register.filter(name='split')
def split(value, key):
    """
      Returns the value turned into a list.
    """
    return value.split(key)


@register.filter()
def to_float(value):
    return float(value)


@register.filter()
def dict_sum(dict):
    result = []
    for k, v in dict:
        result.append(float(k)*float(v))
    return result
