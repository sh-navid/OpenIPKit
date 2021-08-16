from distutils.core import setup
from setuptools import find_packages
import scripts.osHelper as osh
import os


long_description=''
with open(osh.getPath(__file__)+'/README.md' , encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='PyHelper',
    packages=find_packages('.'), 
    version='0.0.1',
    license='MIT',
    description='',
    long_description = long_description,
    long_description_context_type = 'text/markdown',
    author='sh-navid', 
    author_email='',     
    url='',
    download_url='',
    keywords=[],
    install_requires=[],
    classifiers=[]  
)