#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'calvin.zhang'
SITENAME = "zjlog is zj'blog"
SITEURL = ''
PATH = 'content'

# theme and plugins config
THEME = "./themes/pelican-elegant" 
MARKUP = ('md', 'ipynb')
PLUGIN_PATHS = [ './plugins' ]
PLUGINS = ['ipynb.markup','tipue_search','sitemap']
SITEMAP = {                                                                                         
    'format': 'xml',                                                                                
    'priorities': {                                                                                 
        'articles': 1,                                                                              
        'indexes': 0.7,                                                                             
        'pages': 0.5                                                                                
    },                                                                                              
    'changefreqs': {                                                                                
        'articles': 'always',                                                                       
        'indexes': 'always',                                                                        
        'pages': 'always'                                                                           
    }                                                                                               
} 
DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives', 'search', '404'))

# About & project

LANDING_PAGE_ABOUT = {
    "title":"数据挑山工",
    "details":"hello"
}

PROJECTS = [{
    'name': 'Logpad + Duration',
    'url': 'https://github.com/talha131/logpad-plus-duration#logpad--duration',
    'description': 'Vim plugin to emulate Windows Notepad logging feature,'
    ' and log duration of each entry'},
    {'name': 'Elegant Theme for Pelican',
    'url': 'http://oncrashreboot.com/pelican-elegant',
    'description': 'A clean and distraction free theme, with search and a'
    ' lot more unique features, using Jinja2 and Bootstrap'}]

TIMEZONE = 'Asia/Shanghai'
DEFAULT_LANG = 'zh'

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
