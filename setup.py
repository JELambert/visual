# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 22:34:21 2019

@author: Jesus
"""


from setuptools import setup, find_packages
import os

module_dir = os.path.dirname(os.path.abspath(__file__))

setup(
    name='visual',
    version='0.0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='A package to set visual settings',
    long_description=open(os.path.join(module_dir, 'README.md')).read(),
    install_requires=[],
    url='https://github.com/JELambert/visual',
    author=['Joshua E. Lambert'],
    author_email=['joshua.lambert@knights.ucf.edu']
)