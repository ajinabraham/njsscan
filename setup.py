"""Setup for libsast."""
from setuptools import (
    find_packages,
    setup,
)

from pathlib import Path


def read(rel_path):
    init = Path(__file__).resolve().parent / rel_path
    return init.read_text('utf-8', 'ignore')


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            return line.split('\'')[1]
    else:
        raise RuntimeError('Unable to find version string.')


description = ('Something awesome is coming')
setup(
    name='njsscan',
    version=get_version('njsscan/__init__.py'),
    description=description,
    author='Ajin Abraham',
    author_email='ajin25@gmail.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        ('License :: OSI Approved :: '
         'GNU Lesser General Public License v2 (LGPLv2)'),
        'Programming Language :: Python :: 3.7',
    ],
    packages=find_packages(include=[
        'njsscan', 'njsscan.*',
    ]),
    entry_points={
        'console_scripts': [
            'njsscan = njsscan.__main__:main',
            'nodejsscan = njsscan.__main__:main',
        ],
    },
    include_package_data=True,
    url='https://github.com/ajinabraham/njsscan',
    long_description=description,
    install_requires=[
        'colorama>=0.4.3',
    ],
)
