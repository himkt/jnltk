from setuptools import setup, find_packages

setup(
    name = "jnltk",
    version = "0.0.4",
    author = 'himkt',
    author_email = 'himkt@klis.tsukuba.ac.jp',
    description = 'Japanese Natural Language Processing toolkit',
    url = 'https://github.com/himkt/jnltk',

    packages = find_packages(),
    test_suite = 'tests',
)