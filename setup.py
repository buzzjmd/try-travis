# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import find_packages, setup

setup_requirements = [
    'setuptools_scm',
]

setup(
    name='mylib',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    use_scm_version=True,
    setup_requires=setup_requirements,
)
