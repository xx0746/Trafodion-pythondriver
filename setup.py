
import os

import sys

try:
    from setuptools import setup, find_packages

except:
    from distutils.core import setup

version = '0.0.2'

setup(

    name="PyTrafodion",

    version=version,

    description='Pure Python Trafodion Driver',

    long_description="TODO",
    url="https://github.com/CoderSong2015/Trafodion-pythondriver",
    author='Haolin Song',
    author_email='haolin.song@outlook.com',
    packages=find_packages(exclude=['tests*']),
    install_requires=[
        "cryptography",
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Database',
    ],
    keywords="Trafodion",

)

