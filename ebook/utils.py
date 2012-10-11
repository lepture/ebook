import os
import datetime
from jinja2 import Environment, FileSystemLoader
ROOT = os.path.abspath(os.path.dirname(__file__))


def xmldatetime(value):
    if not value:
        return ''
    assert isinstance(value, datetime.datetime)
    return value.strftime("%Y-%m-%dT%H:%M:%SZ")


def utf8(value):
    if isinstance(value, (bytes, type(None), str)):
        return value
    if isinstance(value, int):
        return str(value)
    assert isinstance(value, unicode)
    return value.encode('utf-8')


def render(template, params):
    jinja = Environment(
        loader=FileSystemLoader([os.path.join(ROOT, '_template')]),
        autoescape=False,
    )
    jinja.filters.update({'xmldatetime': xmldatetime})
    tpl = jinja.get_template(template)
    return utf8(tpl.render(params))
