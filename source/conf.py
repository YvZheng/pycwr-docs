# Configuration file for the Sphinx documentation builder.

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
PYCWR_REPO = ROOT / "pycwr"
if PYCWR_REPO.exists():
    sys.path.insert(0, str(PYCWR_REPO))

project = "pycwr"
copyright = "2019-2026, pycwr developers"
author = "Yu Zheng"
release = "1.0.9"
master_doc = "index"

extensions = [
    "nbsphinx",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.coverage",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinx.ext.mathjax",
    "sphinx.ext.todo",
]

nbsphinx_execute = "never"
templates_path = ["_templates"]
language = "zh_CN"
exclude_patterns = []

html_theme = "sphinx_rtd_theme"
html_theme_options = {
    "sticky_navigation": True,
    "collapse_navigation": False,
    "navigation_depth": 4,
    "titles_only": False,
    "style_nav_header_background": "#154c79",
}
html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_title = "pycwr 1.0.9 文档"
html_show_copyright = True
