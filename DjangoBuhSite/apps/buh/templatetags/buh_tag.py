from django import template

from buh import models

register = template.Library()

@register.inclusion_tag('buh/tags/upper_section.html')
def upper_section_tag():
    return {'ignore': 'ignore'}


@register.simple_tag()
def get_site_wrapper_data():
    return models.SiteWrapper.objects.get()

@register.simple_tag()
def index_data():
    return models.Index.objects.get()

@register.simple_tag()
def guarantee_data():
    return models.Guarantee.objects.get()

@register.simple_tag()
def contact_data():
    return models.Contact.objects.get()