# Configuration file for the Sphinx documentation builder.

import os
import sys
sys.path.insert(0, os.path.abspath('../../preclipy'))  # <- adjust if package path differs

# -- Project information -----------------------------------------------------

project = 'PreCliPy'
copyright = '2025, Jayanth Pasupulati'
author = 'Jayanth Pasupulati'
release = '0.1.7'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',     # for Google/NumPy-style docstrings
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'  # ← cleaner and more readable
html_static_path = ['_static']

# -- Autodoc options ---------------------------------------------------------

autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'show-inheritance': True,
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
