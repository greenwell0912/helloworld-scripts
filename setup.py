#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name="helloworld-scripts",
    version="0.1",
    packages=find_packages(),
    
    entry_points={
        "console_scripts": [
            "helloworld=hello.world:main",
        ],
    },
    #install_requires=foo,

    # metadata for upload to PyPI
    #author='Hiroki Yamaguchi',
    #author_email='hiroki6357@gmail.com',
    #description="Hello World Scripts",
    #license='MIT',
    #keywords=["hello world", "console_scripts"],
    #url='https://github.com/greenwell0912/helloworld-scripts',
    
)

