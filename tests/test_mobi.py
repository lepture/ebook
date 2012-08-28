#!/usr/bin/env python
# coding: utf-8

from ebook.lib import Entry, Book
from ebook.mobi import create


def test_create():
    entries = [
        Entry('Hello', 'hello world'),
        Entry('1', '111', category='1'),
        Entry('2', '111', category='1'),
        Entry('3', '111', category='1'),
        Entry(u'中文', '111', category='2'),
    ]
    book = Book('test', entries, lang='zh-CN', uid="test-book")
    create(book, 'build/test1')


def test_periodical():
    entries = [
        Entry('Hello', 'hello world'),
        Entry('1', '111', category='1'),
        Entry('2', '111', category='1'),
        Entry('3', '111', category='1'),
        Entry(u'中文', '111', category='2'),
    ]
    book = Book('test', entries, format='periodical', lang='zh-CN',
                uid="test-periodical")
    create(book, 'build/test2')
