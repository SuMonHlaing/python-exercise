try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
        'description': 'My Project',
        'author': 'Su Mon Hlaing',
        'url': 'URL to get it at.',
        'download_url': 'Where to download it.',
        'author_email': 'sumonhlaing1997@gmail.com',
        'version': '0.1',
        'install_requires': ['nose'],
        'packages': ['ex47']
        'scripts': [],
        'name': 'projectname'
}

setup(**config)