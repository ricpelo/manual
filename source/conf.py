# -*- coding: utf-8 -*-
#
# Manual del proyectista documentation build configuration file, created by
# sphinx-quickstart on Wed Nov 29 11:06:21 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.githubpages',
    'sphinxcontrib.phpdomain',
    'sphinxcontrib.programoutput'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Manual del proyectista'
copyright = u'2017, Ricardo Pérez López'
author = u'Ricardo Pérez López'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = u'1.0'
# The full version, including alpha/beta/rc tags.
release = u'1.0'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'es'

today_fmt = '%B de %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['index_latex.rst']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

highlight_language = 'php'

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_theme_path = ["_themes",]

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    'display_version': False
}

html_title = u'Manual del proyectista'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
html_sidebars = {
    '**': [
        'relations.html',  # needs 'show_related': True theme option to display
        'searchbox.html',
    ]
}

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'hu', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'ru', 'sv', 'tr', 'zh'
#
html_search_language = 'es'

html_context = {
    "display_github": True,
    "github_user": "ricpelo",
    "github_repo": "manual",
    "github_version": "master/source/",
#    "conf_py_path": "/doc/",
    "source_suffix": source_suffix,
}

html_last_updated_fmt = '%d-%m-%Y'

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'Manualdelproyectistadoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    'papersize': 'a4paper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    'pointsize': '12pt',

    # Additional stuff for the LaTeX preamble.
    #
    'fontpkg': r"""
        \usepackage{libertine}
        \setmonofont[
            Path=../../fonts/,
            BoldFont=FiraMono-Bold.ttf,
            AutoFakeSlant,
            BoldItalicFeatures={FakeSlant},
            Scale=MatchLowercase
        ]{FiraMono-Medium.ttf}""",

    'sphinxsetup': """
        verbatimwithframe=false,
        noteBorderColor={rgb}{0.208,0.374,0.486},
        noteborder=1pt""",

    'preamble': r"""
        \usepackage[dotinlabels]{titletoc}
        \usepackage{titlesec}
        \titlelabel{\thetitle.\quad}
        \let\sphinxcodeORI\sphinxcode
        \protected\def\sphinxcode #1%
            {{\color{OuterLinkColor}\sphinxcodeORI{#1}}}
        """,

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc + '_latex', 'manual.tex', u'Manual del proyectista',
     u'Ricardo Pérez López', 'manual'),
]

latex_engine = 'xelatex'

latex_show_urls = 'footnote'

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'manualdelproyectista', u'Manual del proyectista Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'Manualdelproyectista', u'Manual del proyectista Documentation',
     author, 'Manualdelproyectista', 'One line description of project.',
     'Miscellaneous'),
]

from sphinx.highlighting import lexers
from pygments.lexers.web import PhpLexer
lexers['php'] = PhpLexer(startinline=True, linenos=1)
lexers['php-annotations'] = PhpLexer(startinline=True, linenos=1)
primary_domain = 'php'

def setup(app):
    app.add_stylesheet('pygments.css')
    app.add_stylesheet('custom.css')
