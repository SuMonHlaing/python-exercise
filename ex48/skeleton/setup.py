try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
config = {
         'description': 'ex47game',
         'author': 'SuMonHlaing',
         'url': 'URL to get it at.',
         'download_url': 'Where to download it.',
         'author_email': 'sumonhlaing1997@gmail@gmail.com',
         'version': '0.1',
         'install_requires': ['nose'],
         'packages': ['ex47','bin'],
         'scripts': ['weapons'],
         'name': 'ex47game'
         }

setup(**config)