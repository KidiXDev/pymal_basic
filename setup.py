from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'Simple library to get Anime title and ID from MyAnimeList'

# Setting up
setup(
    name="pymal_basic",
    version=VERSION,
    author="KidiXDev",
    author_email="<kidixdev@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['requests'],
    keywords=['mal', 'myanimelist'],
    classifiers=[
        'Development Status :: 1 - Planning',
    ],
)