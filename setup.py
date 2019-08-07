#!/usr/bin/env python3.7

from setuptools import setup

with open('README.md', 'r') as f:
	readme = f.read()

setup(
	name='exc_factory',
	version='0.0.0',
	description='Exception class factory',
	long_description=readme,
	long_description_content_type='text/markdown',
	author='Dull Bananas',
	author_email='dull.bananas0@gmail.com',
	url='https://github.com/dullbananas/exc_factory',
	license='MIT',
	packages=['exc_factory'],
	classifiers=[
		'Development Status :: 4 - Beta',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python :: 3 :: Only',
		'Topic :: Software Development :: Libraries :: Python Modules',
	],
	python_requires='>=3.3',
	install_requires=[
	],
)
