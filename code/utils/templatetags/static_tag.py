from dong_yab.settings import STATIC_URL, VERSION_CSS, VERSION_JS
from django import template

register = template.Library()


@register.simple_tag
def version_css(model_object):
    value = "%s%s?v=%s" % (STATIC_URL, model_object, VERSION_CSS)
    return value


@register.simple_tag
def version_js(model_object):
    value = "%s%s?v=%s" % (STATIC_URL, model_object, VERSION_JS)
    return value

