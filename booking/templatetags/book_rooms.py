import re

from django import template

register = template.Library()

@register.filter
def is_available(room, dates):
    checkin, checkout = dates.split('|')

    return room.is_available(checkin, checkout)


@register.filter
def concatch(value1, value2):
    value1 = re.sub('[|]', '', value1)
    value2 = re.sub('[|]', '', value2)

    return "{}|{}".format(value1, value2)
