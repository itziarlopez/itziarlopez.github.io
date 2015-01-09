#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Itziar Lopez'
SITENAME = u'Spanish Tuition In Vancouver'
SITEURL = u'http://spanishtuition.ca'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Feeds - everything set to none to avoid generating feeds
FEED_ALL_ATOM = ''

# Prevent default pages from being generated - its not necessary for this site
ARCHIVES_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
TAGS_SAVE_AS = ''

# Theme
THEME = 'spanish-tuition-pelican-theme/Output'

# Static Paths/Files
STATIC_PATHS = ['images','static/robots.txt', 'static/CNAME']
EXTRA_PATH_METADATA = {
        'static/robots.txt': {'path': 'robots.txt'},
        'static/CNAME': {'path': 'CNAME'},
}
