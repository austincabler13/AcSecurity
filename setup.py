from setuptools import setup, find_packages

setup(
    name='AcSecurity',
    version='0.1.9',
    packages=find_packages(),
    install_requires=[
        'pip-audit',
        'pylint',
        'argparse',
    ],
    entry_points={
        'console_scripts': [
            'acsecurity=AcSecurity.scanner:main',  # Adjust if your main function is in another file
        ],
    },
    description='A security scanner for applications.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Austin Cabler',
    author_email='austin_cabler@icloud.com',
    url='https://github.com/austincabler13/AcSecurity',
        classifiers=[
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
    'Programming Language :: Python :: 3.13',
    'Programming Language :: Python :: 3.14',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    ],
    python_requires='>=3.12',
)
