# -*- coding: utf-8 -*-
# @Author: jpch89
# @Email:  jpch89@outlook.com
# @Time:   2018/7/28 17:29

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'scanner',
    'author': 'jpch89',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'jpch89@outlook.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex48'],
    'scripts': [],
    'name': 'ex48'
}

setup(**config)
