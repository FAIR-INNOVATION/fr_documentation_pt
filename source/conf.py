# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'FAIRINO Collaborative Robot User Manual'
copyright = '2022-2026, FAIR Innovation (Suzhou) Robotic System Co.,Ltd.'
author = 'FAIR Innovation (Suzhou) Robotic System Co.,Ltd.'
release = '3.9.4'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['recommonmark']

templates_path = ['_templates']
exclude_patterns = []

language = 'de'
locale_dirs = ['locale/']  # 设置本地化数据目录

# 注：在生成html的时候这句话要注释
# latex_engine = 'xelatex'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_css_files = ["custom.css"]
html_logo = '_static/logo.svg'
html_theme_options = {
    'logo_only': True,
    'display_version': False,
}

# highlight_language = "c,c++,python"

# def setup(app):
#     app.add_css_file('_static/custom.css')

# rst_epilog = '\n.. include:: .custom-style.rst\n'