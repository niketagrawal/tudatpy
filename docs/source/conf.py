#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# tudat-api documentation build configuration file, created by
# sphinx-quickstart on Sat May  8 16:14:17 2021.
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
import os
import sys

sys.path.insert(0, os.path.abspath("."))


# -- Multidoc configuration --------------------------------------------------
# Alternative preparation required if building docs on readthedocs.
# if bool(os.getenv("READTHEDOCS")) is True:
#     from document import *
#     from urllib.request import urlopen
#     import json
#     from datetime import datetime

#     multidoc_git_url = "https://github.com/tudat-team/tudat-multidoc.git"
#     multidoc_git_rev = None  # If left at None, latest version is used
#     # multidoc_git_rev = '96d2748ea2a203c797552f56155f1703524f53f6'

#     # Return the latest timestamp of the tudapty conda package for a given label (dev/main)
#     def get_latest_conda_package(label):
#         # Get json data from conda repo
#         response = urlopen(
#             "https://conda.anaconda.org/tudat-team/label/%s/linux-64/repodata.json"
#             % label
#         )
#         data_json = json.loads(response.read())
#         latest_package = 0
#         # Go trough tudatpy packages and find the latest version
#         for package_name, package_info in data_json["packages"].items():
#             if package_name.startswith("tudatpy"):
#                 package_timestamp = package_info["timestamp"]
#                 latest_package = max(latest_package, package_timestamp)
#         return latest_package

#     latest_main_package = get_latest_conda_package("main")
#     print(
#         "Latest main package time:", datetime.fromtimestamp(latest_main_package / 1e3)
#     )
#     latest_dev_package = get_latest_conda_package("dev")
#     print("Latest dev package time:", datetime.fromtimestamp(latest_dev_package / 1e3))

#     # Install the dev version of the tudatpy package if it was the latest to be published
#     install_dev_tudatpy = latest_dev_package >= latest_main_package
#     print(
#         "Tudatpy dev version will%s be installed."
#         % ("" if install_dev_tudatpy else " not")
#     )
#     if install_dev_tudatpy:
#         os.system("conda install -c tudat-team/label/dev tudatpy -y")

#     # clone repository
#     docstring_path = get_docstrings(multidoc_git_url, multidoc_git_rev)

#     # parse api declaration
#     api_declaration = parse_api_declaration(docstring_path, py=True)

#     # source path
#     source_path = generate_documentation(api_declaration, ".")

# else:

# debug only
# print("list files in site packages")
# print(
#     os.listdir(
#         "/home/nagrawal/miniconda3/envs/tudatpy-docs-readthedocs/lib/python3.8/site-packages"
#     )
# )


# Check if running inside a conda environment
conda_prefix = os.getenv("CONDA_PREFIX")
print("conda_prefix:", conda_prefix)
if conda_prefix:
    # Construct the path to the site-packages for the current conda environment
    site_packages_path = os.path.join(conda_prefix, "lib", "python3.8", "site-packages")
else:
    # Fallback or error
    raise EnvironmentError("This script requires a conda environment.")

# Insert the site-packages path to sys.path
sys.path.insert(0, os.path.abspath(site_packages_path))
print("sys.path:", sys.path)

# sys.path.insert(
#     0,
#     os.path.abspath(
#         "/home/nagrawal/miniconda3/envs/tudatpy-docs-readthedocs/lib/python3.8/site-packages"
#     ),
# )


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.autosummary",
    "sphinx.ext.todo",
    "sphinx.ext.coverage",
    "sphinx.ext.mathjax",
    "sphinx.ext.ifconfig",
    "sphinx.ext.viewcode",
    "sphinx.ext.githubpages",
    "sphinxcontrib.napoleon",
    "sphinx.ext.autosectionlabel",
    "sphinx_copybutton",
    # 'breathe',
    # 'exhale'
]
autosummary_generate = True  # Turn on sphinx.ext.autosummary

add_module_names = False
autodoc_member_order = "groupwise"

# napoleon_type_aliases = {
#     "Dict": ":class:`~typing.Dict`",
#     "Callable": ":class:`~typing.Callable`",
#     "List": ":class:`~typing.List`",
# }


# to not skip __init__
# def skip(app, what, name, obj, would_skip, options):
#     if name == "__init__":
#         return False
#     return would_skip
#
#
# def setup(app):
#     app.connect("autodoc-skip-member", skip)


# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "TudatPy API"
copyright = "2021, Tudat Team"
author = "Tudat Team"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = ""
# The full version, including alpha/beta/rc tags.
release = ""

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'sphinx_rtd_theme'
html_theme = "furo"
html_theme_options = {
    "navigation_with_keys": True,
    "announcement": "<em>These docs are a work-in-progress!</em>",
}

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
html_css_files = [
    "style.css",
]
# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
# html_sidebars = {
#     '**': [
#         'relations.html',  # needs 'show_related': True theme option to display
#         'searchbox.html',
#     ]
# }

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "TudatPy API"
html_title = "TudatPy API Reference"

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, "tudat-api.tex", "TudatPy API", "John", "manual"),
]

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, "tudat-api", "TudatPy API", [author], 1)]

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "tudat-api",
        "TudatPy API",
        author,
        "tudat-api",
        "One line description of project.",
        "Miscellaneous",
    ),
]

# Example configuration for intersphinx: refer to the Python standard library.

# intersphinx_mapping = {'https://docs.python.org/': None}

intersphinx_mapping = {
    "python": ("https://docs.python.org/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
    "pagmo": ("https://esa.github.io/pagmo2/", None),
    "numpy": ("http://docs.scipy.org/doc/numpy/", None),
    "scipy": ("http://docs.scipy.org/doc/scipy/reference/", None),
    "matplotlib": ("https://matplotlib.org/stable/api/", None),
}
