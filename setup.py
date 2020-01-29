from setuptools import setup

setup(
    name='squidbio',
    version='0.1',
    description='A CLI for the SquidBio platform',
    url='http://github.com/SquidBio/squidbio-cli',
    author='Isaac Ellmen',
    author_email='isaac@squidbio.com',
    packages=['squidbio'],
    entry_points={
        'console_scripts': ['squidbio=squidbio.command_line:main'],
    }
)
