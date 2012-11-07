import os
import re
import urlparse
import datetime
import hashlib
import gevent
import urllib
from jinja2 import Environment, FileSystemLoader
ROOT = os.path.abspath(os.path.dirname(__file__))


def xmldatetime(value):
    if not value:
        return ''
    assert isinstance(value, datetime.datetime)
    return value.strftime("%Y-%m-%d %H:%M:%S")


def hostname(url):
    if not url:
        return ''
    hostname = urlparse.urlparse(url).hostname
    if hostname.startswith('www.'):
        return hostname[4:]
    return hostname


def md5image(link):
    if link.startswith('http://') or link.startswith('https://'):
        name = hashlib.md5(link).hexdigest()
        if link.endswith('.png'):
            ext = 'png'
        elif link.endswith('.gif'):
            ext = 'gif'
        else:
            ext = 'jpg'
        return '%s.%s' % (name, ext)
    return link


def local_image(content):
    def replace(m):
        link = m.group(2)
        return 'src="images/%s"' % md5image(link)
    pattern = re.compile(r'''src=('|")(\S+?)\1''')
    content = pattern.sub(replace, content)
    return content


def media_type(link):
    if link.endswith('.png'):
        return 'image/png'
    if link.endswith('.gif'):
        return 'image/gif'
    return 'image/jpeg'


def download(links, folder):
    if not links:
        return

    if not os.path.exists(folder):
        os.makedirs(folder)

    from gevent import monkey
    monkey.patch_all()

    def fetch(folder, link):
        if link.startswith('http://') or link.startswith('https://'):
            filename = os.path.join(folder, md5image(link))
            if os.path.exists(filename):
                return
            urllib.urlretrieve(link, filename)

    jobs = [gevent.spawn(fetch, folder, link) for link in links]
    gevent.joinall(jobs)


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
    jinja.filters.update({
        'xmldatetime': xmldatetime,
        'hostname': hostname,
        'md5image': md5image,
        'media_type': media_type,
        'local_image': local_image,
    })
    tpl = jinja.get_template(template)
    return utf8(tpl.render(params))
