# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
from pathlib import Path

DOCS_DIR = Path(__file__).resolve().parent
REPO_ROOT = DOCS_DIR.parent
sys.path.insert(0, str(REPO_ROOT))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Carbox'
copyright = '2026, Suleiman M Hajizadeh & Garib N Murshudov'
author = 'Suleiman M Hajizadeh & Garib N Murshudov'
release = '0.4.5'
version = '0.4.5'

# Base URL for canonical links and search engine discovery
html_baseurl = 'https://project-carbox.readthedocs.io/en/latest/'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.mathjax',
]
try:
    import sphinx_sitemap  # noqa: F401
    extensions.append('sphinx_sitemap')
except ImportError:
    pass

# Sitemap configuration
sitemap_url_scheme = '{link}'

# Global metadata for Search Engine Optimization (SEO / Google / Bing)
html_meta = {
    'google-site-verification': 'med3XHPJzcSjHLpdN-jmNKekn-MFZcQE8IwPeFbCk7o',
    'google-site-verification-secondary': 'lbqn6nIPchEP3d12Vf4UQmQpyKhJ1Mzq-di2S-t3rF0',
    'description': 'Official scientific documentation for Project Carbox: high-throughput macromolecular crystallographic validation, anomalous carboxyl protonation, Servalcat refinement, and Low-Barrier Hydrogen Bond (LBHB) discovery by Suleiman M Hajizadeh & Prof. Garib N Murshudov.',
    'keywords': 'Carbox, Project Carbox, Carbox Platform, Carbox CLI, Carbox Python API, Suleiman M Hajizadeh, Suleiman Hajizadeh, Süleyman M Hacızadə, Garib N Murshudov, Garib Murshudov, Qərib N Mürşüdov, MRC Laboratory of Molecular Biology, MRC LMB Cambridge, Institute of Molecular Biology, Western Caspian University, Macromolecular Crystallography, Protein Crystallography, Structural Biology, Structural Bioinformatics, Anomalous Carboxyl Protonation, Carboxyl Protonation States, Shared Protons, Low-Barrier Hydrogen Bond, LBHB, Short Strong Hydrogen Bond, SSHB, Dielectric Shielding, Born Desolvation Energy, PROPKA 3, pKa Shift Calculation, REFMAC5, Servalcat, Gemmi, Tukey IQR B-factor Outlier, Fisher Z RSCC, Electron Density Map Validation, 2mFo-DFc Map Carving, 1KZK, 1OEW, 2DSX, 1FKN, Endothiapepsin, Rubredoxin, BACE1, HIV-1 Protease, bioinformatika Azərbaycan, kristalloqrafiya',
    'author': 'Suleiman M Hajizadeh & Garib N Murshudov',
    'robots': 'index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1',
    'googlebot': 'index, follow',
    'og:title': 'Carbox Documentation | Project Carbox',
    'og:description': 'Official scientific documentation for Project Carbox: high-throughput macromolecular crystallographic validation, anomalous carboxyl protonation, Servalcat refinement, and LBHB discovery.',
    'og:type': 'website',
    'og:url': 'https://project-carbox.readthedocs.io/en/latest/',
    'og:image': 'https://raw.githubusercontent.com/project-carbox/project-carbox.github.io/main/assets/carbox_logo.svg',
    'twitter:card': 'summary_large_image',
    'twitter:title': 'Carbox Documentation | Project Carbox',
    'twitter:description': 'Official scientific documentation for Project Carbox: crystallographic validation, anomalous carboxyl protonation, and LBHB discovery.',
    'twitter:image': 'https://raw.githubusercontent.com/project-carbox/project-carbox.github.io/main/assets/carbox_logo.svg',
}

# Mock scientific dependencies to ensure lightweight and reliable builds on Read the Docs
autodoc_mock_imports = [
    'gemmi',
    'numpy',
    'scipy',
    'pandas',
    'matplotlib',
    'seaborn',
    'tqdm',
    'propka',
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

root_doc = 'index'

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '.venv', 'venv']
suppress_warnings = ['myst.header', 'misc.highlighting_failure']

# MyST Markdown Parser options
myst_enable_extensions = [
    'dollarmath',
    'amsmath',
    'deflist',
    'html_admonition',
    'html_image',
    'colon_fence',
]
myst_heading_anchors = 3

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['assets']
html_extra_path = ['robots.txt']
html_title = 'Carbox Documentation'
html_logo = 'assets/carbox_logo.png'
html_favicon = 'assets/carbox_logo.png'

html_theme_options = {
    'logo_only': False,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': True,
    'navigation_depth': 4,
    'collapse_navigation': False,
    'sticky_navigation': True,
    'includehidden': True,
    'titles_only': False,
}
