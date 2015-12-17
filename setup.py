#!/usr/bin/python
#
# This file is part of PlainForm
# Copyright © 2015 Guillaume Ayoub
#
# BSD-Licensed


"""
PlainForm
=========

Formidable forms formed with WTForms.

"""

from setuptools import setup
import re
import os

with open(
        os.path.join(os.path.dirname(__file__), 'plainform.py'),
        encoding='utf-8') as fd:
    __version__ = re.search("__version__ = '([^']+)'", fd.read()).group(1)

setup(
    name='plainform',
    version=__version__,
    description='Formidable forms formed with WTForms.',
    long_description=__doc__,
    author='Guillaume Ayoub',
    author_email='guillaume.ayoub@kozea.fr',
    download_url=(
        'http://pypi.python.org/packages/source/p/plainform/'
        'plainform-%s.tar.gz' % __version__),
    license='GNU GPL v3',
    platforms='Any',
    py_modules=['plainform'],
    provides=['plainform'],
    keywords=['html', 'forms'],
    install_requires=['wtforms>=2.1'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'
    ]
)
