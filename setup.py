## setup.py
from setuptools import setup, find_packages

setup(
    name='AcSecurity',
    version='1.2.3',
    packages=find_packages(),
    install_requires=[
        'pip-audit',
        'pylint',
        'argparse',
        'pytest',
    ],
    entry_points={
    'console_scripts': [
        'acsecurity=src.scanner:main',
    ],
},

    description='A security scanner for applications.',
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type='text/markdown',
    author='Austin Cabler',
    author_email='austin_cabler@icloud.com',
    url='https://github.com/austincabler13/AcSecurity',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.12',
)

## Copyright (C) 2024  Austin Cabler
