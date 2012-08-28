#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
kwargs = {}
major, minor = sys.version_info[:2]
if major >= 3:
    kwargs['use_2to3'] = True

from setuptools import setup
install_requires = ['Jinja2']


import ebook
from email.utils import parseaddr
author, author_email = parseaddr(ebook.__author__)

setup(
    name='ebook',
    version=ebook.__version__,
    author=author,
    author_email=author_email,
    #url=ebook.__homepage__,
    packages=['ebook'],
    description='ebook library for mobi and epub',
    #long_description=open('README.rst').read(),
    license='BSD License',
    install_requires=install_requires,
    include_package_data=True,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    **kwargs
)
