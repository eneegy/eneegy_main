# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in eneegy_main/__init__.py
from eneegy_main import __version__ as version

setup(
	name='eneegy_main',
	version=version,
	description='Main Page',
	author='Eneegy',
	author_email='eneegy.ltd@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
