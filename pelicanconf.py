#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Ry Whittington'
SITENAME = 'Test Blog'
SITEURL = 'http://localhost:8000'
THEME = 'pelican-themes/pelican-blue_'
PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Menu
MENUITEMS = [
    ['Blog', SITEURL],
    ['About', 'https://www.linkedin.com/in/rywhittington/'],
]

# Blogroll
LINKS = (
    ('Pelican', 'https://getpelican.com/'),
)

# Social widget
SOCIAL = (
    ('linkedin', 'https://www.linkedin.com/in/rywhittington/'),
    ('github', 'https://github.com/rwhitt2049'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
