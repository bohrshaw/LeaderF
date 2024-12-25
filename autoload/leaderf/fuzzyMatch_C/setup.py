# -*- coding: utf-8 -*-
import os
from setuptools import setup, Extension

# Define the extensions
module1 = Extension(
    "fuzzyMatchC",
    sources=["fuzzyMatch.c"]
)

module2 = Extension(
    "fuzzyEngine",
    sources=["fuzzyMatch.c", "fuzzyEngine.c"]
)

# Setup script
setup(
    name="fuzzyEngine",
    version="2.0",
    description="Fuzzy match algorithm written in C.",
    author="Yggdroot",
    author_email="archofortune@gmail.com",
    url="https://github.com/Yggdroot/LeaderF",
    license="Apache License 2.0",
    ext_modules=[module1, module2]
)
