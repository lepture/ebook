#!/usr/bin/env python

import os
import subprocess

from utils import utf8, xmldatetime
from jinja2 import Environment, FileSystemLoader


ROOT = os.path.abspath(os.path.dirname(__file__))


def render(template, params):
    jinja = Environment(
        loader=FileSystemLoader([os.path.join(ROOT, '_mobi')]),
        autoescape=False,
    )
    jinja.filters.update({'xmldatetime': xmldatetime})
    tpl = jinja.get_template(template)
    return utf8(tpl.render(params))


def create(book, destination):
    folder = os.path.abspath(destination)
    if not os.path.isdir(folder):
        os.makedirs(folder)

    # write content.html
    f = open(os.path.join(folder, 'content.html'), 'w')
    html = render('content.html', {'book': book})
    f.write(html)
    f.close()

    # write toc.ncx
    f = open(os.path.join(folder, 'toc.ncx'), 'w')
    html = render('toc.ncx', {'book': book})
    f.write(html)
    f.close()

    # write content.opf
    opf = os.path.join(folder, 'content.opf')
    f = open(opf, 'w')
    html = render('content.opf', {'book': book})
    f.write(html)
    f.close()

    if 'KINDLEGEN' in os.environ:
        kindlegen = os.environ['KINDLEGEN']
    else:
        kindlegen = 'kindlegen'

    output = "%s.mobi" % book.uid
    subprocess.call([kindlegen, opf, '-o', output])
    return
