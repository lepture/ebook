#!/usr/bin/env python
# coding: utf-8

from ebook.lib import Entry, Book
from ebook.mobi import create


def test_mobi_create():
    entries = [
        Entry('Hello', 'hello world'),
        Entry('1', '111', category='1'),
        Entry('2', '111', category='1'),
        Entry('3', '111', category='1'),
        Entry(u'中文', '111', category='2'),
    ]
    book = Book('test', entries, lang='zh-CN')
    create(book, 'build')
