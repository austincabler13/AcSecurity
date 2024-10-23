from setuptools import setup, find_packages

setup(
    name='AcSecurity',
    version='0.2',
    packages=find_packages(),
    install_requires=[
        'pylint',  # Add any other dependencies here
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
    url='https://github.com/yourusername/AcSecurity',  # Your repository URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # Change if using a different license
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Adjust as needed
)
