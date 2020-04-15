"""Setup for libsast."""
from setuptools import (
    find_packages,
    setup,
)

description = ('Something awesome is coming')
setup(
    name='njsscan',
    version='0.0.1',
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
        ],
    },
    include_package_data=True,
    url='https://github.com/ajinabraham/njsscan',
    long_description=description,
    install_requires=[],
)
