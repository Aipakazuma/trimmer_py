import os
from setuptools import setup, find_packages


# Package meta-data.
NAME = 'trimmer_py'
DESCRIPTION = 'trimmer.'
AUTHOR = 'aipa'
EMAIL = ''
URL = ''

# What packages are required for this module to be executed?
REQUIRED = [
    'beautifulsoup4'
]

here = os.path.abspath(os.path.dirname(__file__))

# Load the package's __version__.py module as a dictionary.
about = {}
with open(os.path.join(here, NAME, '__version__.py')) as f:
    exec(f.read(), about)

setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    install_requires=REQUIRED,
    include_package_data=True,
    dependency_links=[],
    license='',
    packages=find_packages(exclude=('tests', 'docs')),
    test_suite='tests'
)
