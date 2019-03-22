from django import template
from django.template.defaultfilters import stringfilter
from ..models import StructureTypeChoice

register = template.Library()


@register.filter
@stringfilter
def structure_type(value):
    return StructureTypeChoice(value).name
