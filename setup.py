#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages, Extension

with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = ['Click>=7.0', 'ffmpy>=0.2.3', 'spotipy>=2.16.1', 'youtube-dl>=2020.11.1.1', ]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest>=3', ]

setup(
    author="Laurence Rawlings",
    author_email='contact@laurencerawlings.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Tool for downloading Spotify songs to MP3 - Full Metadata & Cover Art",
    entry_points={
        'console_scripts': [
            'savify=savify.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme,
    include_package_data=True,
    keywords='savify, spotify, downloader, mp3, save, playlist',
    name='savify',
    packages=find_packages(include=['savify', 'savify.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/LaurenceRawlings/savify',
    version='0.1.0',
    zip_safe=False,
)