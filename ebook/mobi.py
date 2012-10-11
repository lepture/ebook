#!/usr/bin/env python

import os
import subprocess
from utils import render, download


ROOT = os.path.abspath(os.path.dirname(__file__))


def create(book, destination):
    if destination.endswith('.mobi'):
        folder, output = os.path.split(destination)
    else:
        folder = destination
        output = '%s.mobi' % book.uid
    folder = os.path.abspath(folder)
    if not os.path.isdir(folder):
        os.makedirs(folder)

    # download images
    download(book.images, os.path.join(folder, 'images'))

    # write content.html
    f = open(os.path.join(folder, 'content.html'), 'w')
    html = render('mobi/content.html', {'book': book})
    f.write(html)
    f.close()

    # write toc.ncx
    f = open(os.path.join(folder, 'toc.ncx'), 'w')
    html = render('mobi/toc.ncx', {'book': book})
    f.write(html)
    f.close()

    # write content.opf
    opf = os.path.join(folder, 'content.opf')
    f = open(opf, 'w')
    html = render('mobi/content.opf', {'book': book})
    f.write(html)
    f.close()

    if 'KINDLEGEN' in os.environ:
        kindlegen = os.environ['KINDLEGEN']
    else:
        kindlegen = 'kindlegen'

    subprocess.call([kindlegen, opf, '-o', output])
    return
