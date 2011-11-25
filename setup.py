from distutils.core import setup
from setuptools import setup, find_packages

setup(
    name = 'favorites',
    version = '0.1',
    description = 'Generic favorites application for Django',
    author = 'Andrew Gwozdziewycz',
    author_email = 'git@apgwoz.com',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests', 'docs']),
    classifiers = ['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Utilities'],
)
