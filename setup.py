from setuptools import setup, find_packages

setup(
    name='AcSecurity',
    version='0.3',
    packages=find_packages(),
    install_requires=[
        'pip-audit',
        'pylint',

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
        'Programming Language :: Python :: 3.12',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3',
)
