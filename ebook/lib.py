#!/usr/bin/env python

import re
import datetime


class Entry(object):
    def __init__(self, title, content, uid=None, author=None,
                 category='default', created=None, url=None):
        self.title = title

        self.content = content

        self.uid = uid or title
        self.author = author or ''
        self.category = category
        self.created = created
        self.url = url

    @property
    def images(self):
        pattern = re.compile(r'''src=('|")(\S+?)\1''')
        for m in pattern.findall(self.content):
            yield m[1]


class Category(object):
    def __init__(self, title, uid=None):
        self.title = title
        self.uid = uid or title
        self.entries = []

    def __repr__(self):
        return self.title

    def __str__(self):
        return self.title

    def append(self, entry):
        self.entries.append(entry)


class Book(object):
    def __init__(self, title, entries, description=None, author='',
                 periodical=False, subject=None, lang='en-US', uid=None,
                 created=None, creator='lepture', publisher='ebook'):
        self.title = title
        self.entries = entries
        self.description = description or ''

        self.author = author
        self.periodical = periodical

        self.subject = subject or title
        self.lang = lang
        self.uid = uid or title

        self.created = created or datetime.datetime.utcnow()
        self.creator = creator
        self.publisher = publisher

    @property
    def categories(self):
        cats = {}
        for entry in self.entries:
            if entry.category not in cats:
                cats[entry.category] = Category(entry.category)
            cats[entry.category].append(entry)

        return cats.values()

    @property
    def images(self):
        images = []
        for entry in self.entries:
            images.extend(entry.images)
        return images
