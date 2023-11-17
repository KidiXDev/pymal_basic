from setuptools import setup, find_packages
from pathlib import Path

VERSION = '0.0.2'
DESCRIPTION = 'Simple library to get Anime title and ID from MyAnimeList'

this_directory = Path(__file__).parent
LONG_DESCRIPTION = (this_directory / 'README.md').read_text()

# Setting up
setup(
    name="pymal_basics",
    version=VERSION,
    author="KidiXDev",
    author_email="<kidixdev@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url='https://github.com/KidiXDev/pymal_basic',
    packages=find_packages(),
    license='MIT',
    install_requires=[],
    keywords=['mal', 'myanimelist'],
    classifiers=[
        'Development Status :: 1 - Planning',
    ],
)