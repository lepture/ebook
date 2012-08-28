#!/usr/bin/env python

import datetime


class Entry(object):
    def __init__(self, title, content, uid=None, author=None, category=None,
                 created=None, url=None):
        self.title = title
        self.content = content
        self.uid = uid or title
        self.author = author or ''
        self.category = category
        self.created = created
        self.url = url


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
                 format='book', subject=None, lang='en-US', uid=None,
                 created=None, creator='lepture', publisher='ebook'):
        self.title = title
        self.entries = entries
        self.description = description or ''

        self.author = author
        self.format = format

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
            if entry.category and entry.category not in cats:
                cats[entry.category] = Category(entry.category)

            cats[entry.category].append(entry)

        return cats.itervalues()
