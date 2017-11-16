#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Austin Green'
SITENAME = "Austin Green's Blog"
SITEURL = ''
SITELOGO = ''
FAVICON = '/images/favicon.ico'

PATH = 'content'
STATIC_PATHS = ['images']

TIMEZONE = 'America/Chicago'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
GITHUB_URL = 'https://github.com/ausgreen'

THEME = "./themes/Flex"
# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),)

# Social widget
SOCIAL = (('GitHub', 'https://github.com/ausgreen'),)

DEFAULT_PAGINATION = False
DISPLAY_PAGES_ON_MENU = True

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
