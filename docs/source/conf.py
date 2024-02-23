# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Pizza'
copyright = '2023, Graziella'
author = 'Cook'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'myst_parser',
    'sphinx_external_toc',
]
external_toc_exclude_missing = True


intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['css']
html_css_files = ['IBIS-docs.css']
html_logo = 'Trusted-ID hele logo-23.svg'

# -- Options for EPUB output
epub_show_urls = 'footnote'
