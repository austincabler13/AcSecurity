from setuptools import setup, find_packages
import os

setup(
    name='AcSecurity',
    version='1.1.1',
    packages=find_packages(),
    install_requires=[
        'pip-audit',
        'pylint',
        'argparse',
        'pytest',
    ],
    entry_points={
        'console_scripts': [
            'acsecurity=AcSecurity.run_scanner:main',
        ],
    },
    description='A security scanner for applications.',
    long_description=open(os.path.join("docs", "README.md")).read(),  # Fix the path here
    long_description_content_type='text/markdown',
    author='Austin Cabler',
    author_email='austin_cabler@icloud.com',
    url='https://github.com/austincabler13/AcSecurity',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.12',
)
