from setuptools import setup


setup(
  name = 'pypdb',
  packages = ['pypdb'], # same as 'name'
  version = '0.5',
  install_requires=[
        'xmltodict', 
        'beautifulsoup4'
  ],
  description = 'A Python wrapper for the Protein Data Bank (PDB) API',
  author = 'William Gilpin',
  author_email = 'firstnamelastname(as one word)@googleemailservice',
  url = 'https://github.com/williamgilpin/pypdb',
  download_url = 'https://github.com/williamgilpin/pypdb/tarball/0.2', 
  keywords = ['protein','data','RESTful','api'],
  classifiers = [],
)
