#!/usr/bin/env python
# -*- coding: utf-8 -*-

# placeholder to get gh pages to work

try:
    from setuptools import setup
except:
    from distutils.core import setup


requirements = ['numpy >= 1.25', 'matplotlib', 'astropy >= 6.0', 'shapely']
setup_requirements = ['numpy']

setup(
    author='Regions Developers',
    author_email='astropy.team@gmail.com',
    python_requires='>=3.11',
    classifiers=[
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Cython',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Astronomy',
    ],
    description='An Astropy coordinated package for region handling',
    install_requires=requirements,
    setup_requires=setup_requirements,
    license='BSD-3-Clause'
    long_description='README.rst',
    name='regions',
)
