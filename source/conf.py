# Configuration file for the Sphinx documentation builder.

# -- Path setup --------------------------------------------------------------
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import sphinx_rtd_theme
import sphinx_fontawesome

# -- Project information -----------------------------------------------------
project = 'sample-docs'
copyright = '2022, Hiroki Yamagishi'
author = 'Hiroki Yamagishi'

# -- General configuration ---------------------------------------------------
extensions = ['sphinx_rtd_theme', 'sphinx_fontawesome', 'myst_parser']
source_suffix = {'.rst': 'restructuredtext', '.md': 'markdown'}
templates_path = ['_templates']
language = 'ja'
exclude_patterns = ['build']

# -- Options for HTML output -------------------------------------------------
html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_show_sourcelink = False
html_static_path = ['_static']
