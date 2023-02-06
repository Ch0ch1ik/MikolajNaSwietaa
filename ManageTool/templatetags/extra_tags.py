from django import template

from ManageTool.models import Order, Applications

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
        result.append(float(k) * float(v))
    return result


@register.filter()
def part_sum(tuple):
    result = 0
    for item in tuple:
        result += float(item[0]) * float(item[1])
    return result


@register.filter()
def orders_by_province(province):
    orders = Order.objects.all().filter(province=province)
    return orders


@register.filter()
def applications_by_region(region):
    applications = Applications.objects.all().filter(work_region=region)
    return applications


@register.filter()
def remove_spaces(string_with_spaces):
    string_without_spaces = string_with_spaces.replace(" ", "_")
    return string_without_spaces


@register.filter()
def vat(value):
    result = value * 1.23
    return round(result, 2)
