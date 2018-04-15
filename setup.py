#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name="helloworld-scripts",
    version="0.0.1",
    py_modules=['world'],
    package_dir={'': 'hello'},
    install_requires=open('requirements.txt').read().splitlines(),
    description="Hello World Scripts",
    #long_description=open('README.txt').read(),
    author='Hiroki Yamaguchi',
    author_email='hiroki6357@gmail.com',
    url='https://github.com/greenwell0912/helloworld-scripts',
    keywords=["hello world", "console_scripts"],
    license='MIT',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.5.2",
    ],
    entry_points={
        "console_scripts": [
            "helloworld=world:main",
        ],
    },
)

