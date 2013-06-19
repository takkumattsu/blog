# -*- coding: utf-8 -*-

import tinkerer
import tinkerer.paths        
import sys, os

# **************************************************************
# TODO: Edit the lines below
# **************************************************************

# Change this to the name of your blog
project = 'Life is like a development.'                   

# Change this to the tagline of your blog
tagline = u'メモ、備忘録'                  

# Change this to the description of your blog
description = ''

# Change this to your name
author = 'TakkuMattsu'

# Change this to your copyright string
copyright = '2013, ' + author         

# Change this to your blog root URL (required for RSS feed)
website = 'http://www.nanao-a.com'                              

# Language
language = 'ja'

# pygment
pygments_style = 'native'

# **************************************************************
# More tweaks you can do
# **************************************************************

# Add your Disqus shortname to enable comments powered by Disqus
disqus_shortname = 'takkumattsu'

# Change your favicon (new favicon goes in _static directory)
html_favicon = 'tinkerer.ico'

# Pick another Tinkerer theme or use your own
html_theme = "custom_minimal"

# Theme-specific options, see docs
html_theme_options = { }                                  

# Link to RSS service like FeedBurner if any, otherwise feed is
# linked directly
rss_service = None

# Number of blog posts per page
posts_per_page = 1

# **************************************************************
# Edit lines below to further customize Sphinx build
# **************************************************************

# Add other Sphinx extensions here
extensions = ['tinkerer.ext.blog', 'tinkerer.ext.disqus', 'sphinxcontrib.twitter', 'sphinxcontrib.blockdiag'] 

# Fontpath for blockdiag (truetype font)
current_dir = os.path.abspath(os.path.dirname(unicode(__file__)))
my_fonts_path = current_dir + '/fonts/TakaoGothic.ttf'

blockdiag_fontpath = [ my_fonts_path, # my setting
                       'C:\Windows\Fonts\msmincho.ttc', # for Windows
                       '/Library/Fonts/Osaka.ttf', # for Mac OS
                       '/usr/share/fonts/truetype/ipafont/ipagp.ttf', # for Linux
                     ]

# Add other template paths here
templates_path = ['_templates']

# Add other static paths here
html_static_path = ['_static', tinkerer.paths.static]

# Custom css
def setup(app):
    app.add_stylesheet('custom.css')

# Add other theme paths here
html_theme_path = ['_themes', tinkerer.paths.themes]                 

# Add file patterns to exclude from build
exclude_patterns = ["drafts/*", "_templates/*"]

# Add templates to be rendered in sidebar here
html_sidebars = {
    "**": ["gravatar.html", "twitter.html","recent.html", "categories.html", "tags.html" ]
}

# **************************************************************
# Do not modify below lines as the values are required by 
# Tinkerer to play nice with Sphinx
# **************************************************************

source_suffix = tinkerer.source_suffix
master_doc = tinkerer.master_doc
version = tinkerer.__version__
release = tinkerer.__version__
html_title = project
html_use_index = False
html_show_sourcelink = False
html_add_permalinks = None
