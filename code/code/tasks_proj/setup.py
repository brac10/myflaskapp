"""Minimal setup file for tasks project."""

from setuptools import setup, find_packages

setup(
    name='tasks',
    version='0.1.1',
    license='proprietary', 
    description='RangerPI MVP Example',

    author='Scott Braconnier',
    author_email='email if you need help.',
    url='https://www.bracom.org',

    packages=find_packages(where='src'),
    package_dir={'': 'src'},

    install_requires=['click==7.1.2', 'tinydb==3.15.1', 'six', 'pytest', 'pytest-mock'],
    tests_require=['pytest', 'pytest-mock'],
    extras_require={'mongo': 'pymongo'},

    entry_points={
        'console_scripts': [
            'tasks = tasks.cli:tasks_cli',
        ]
    },
)
