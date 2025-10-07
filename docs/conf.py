import os
import sys

# --- Informations sur le projet ---
project = "OC Projet 13"
author = "Matthieu Chambon"
release = "1.0"
copyright = "%Y, Matthieu Chambon"

# --- Chemin du projet pour les imports Python ---
sys.path.insert(0, os.path.abspath(".."))

# --- Extensions Sphinx ---
extensions = [
    "sphinx.ext.autodoc",      # Génération auto de doc à partir du code Python
    "sphinx.ext.viewcode",     # Liens vers le code source
]

# --- Fichiers sources ---
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

# --- Fichier racine ---
master_doc = "index"

# --- Thème ---
html_theme = "sphinx_rtd_theme"
