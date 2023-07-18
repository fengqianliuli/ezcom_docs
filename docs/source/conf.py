# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'EZcom'
copyright = '2023, haotian.shi'
author = 'haotian.shi'
release = 'v0.2.0'


# -- General configuration

extensions = [
    'breathe',
    'exhale',
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'recommonmark',
    'sphinx_markdown_tables',
]

breathe_projects = {
    "EZcom": "doxygen/xml",
}
breathe_default_project = "EZcom"

# # Setup the exhale extension
# exhale_args = {
#     # These arguments are required
#     "containmentFolder":     "./api",
#     "rootFileName":          "library_root.rst",
#     "doxygenStripFromPath":  "..",
#     # Heavily encouraged optional argument (see docs)
#     "rootFileTitle":         "Library API",
#     # Suggested optional arguments
#     "createTreeView":        True,
#     # TIP: if using the sphinx-bootstrap-theme, you need
#     # "treeViewIsBootstrap": True,
#     "exhaleExecutesDoxygen": True,
#     "exhaleDoxygenStdin":    "INPUT = ../include"
# }

source_suffix = {
  '.rst': 'restructuredtext',
  '.md': 'markdown'
}

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

language = 'zh_CN'

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# -- Options for EPUB output
epub_show_urls = 'footnote'
