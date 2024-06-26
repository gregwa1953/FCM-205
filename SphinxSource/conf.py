# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Sphinx Demo Program'
copyright = '2024, Gregory Walters'
author = 'Gregory Walters'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here.
#PYTHONPATH='/home/greg/Desktop/pagetests/Page8.1f/SphinxDemo1'
import pathlib
import sys
#sys.path.insert(0, pathlib.Path(__file__).parents[2].resolve().as_posix())
sys.path.append('/home/greg/Desktop/pagetests/Page8.1f/SphinxDemo1')
print(f"{sys.path=}")
extensions = [
'sphinx.ext.duration',
'sphinx.ext.doctest',
'sphinx.ext.autodoc',
'sphinx.ext.autosummary']

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'bizstyle'
html_static_path = ['_static']
