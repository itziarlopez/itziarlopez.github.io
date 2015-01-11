#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://spanishtuition.ca'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

# Feeds - everything set to none to avoid generating feeds
FEED_ALL_ATOM = ''

# Theme For Production
THEME = 'spanish-tuition-pelican-theme/Output_Production'

# Plugins 
PLUGINS = [
    'sitemap'
]

# Sitemap Plugin
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.75,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'weekly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}
