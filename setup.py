import io
import os
from setuptools import setup, find_packages

VERSION = '0.1'

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()


setup(
    name='runcode',
    version=VERSION,
    author='Micro Pyramid Informatic Pvt. Ltd.',
    author_email='hello@micropyramid.com',
    url='https://github.com/runcode-io/runcode-python',
    description='RunCode Python API',
    long_description=README,
    packages=find_packages(exclude=['tests', 'tests.*']),
    include_package_data=True,
    install_requires=[
        'requests'
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Internationalization',
    ],
)
