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
import plainform


setup(
    name='plainform',
    version=plainform.VERSION,
    description='Formidable forms formed with WTForms.',
    long_description=__doc__,
    author='Guillaume Ayoub',
    author_email='guillaume.ayoub@kozea.fr',
    download_url=(
        'http://pypi.python.org/packages/source/p/plainform/'
        'plainform-%s.tar.gz' % plainform.VERSION),
    license='GNU GPL v3',
    platforms='Any',
    py_modules=['plainform'],
    provides=['plainform'],
    keywords=['html', 'forms'],
    install_requires=['wtforms>=2.0'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4'])
