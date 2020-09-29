#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="steven armour",
    author_email='audreyr@example.com',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Test on how to get fire v3 usage working withsetup tools on windows",
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='test_cli_fire_cookie',
    name='test_cli_fire_cookie',
    packages=find_packages(include=['test_cli_fire_cookie', 'test_cli_fire_cookie.*', 'test_cli_fire_cookie.action']),
    entry_points={
        "console_scripts": ["test_cli_fire = test_cli_fire_cookie.test_cli_fire_cookie:main"]
    },
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/audreyr/test_cli_fire_cookie',
    version='0.1.0',
    zip_safe=False,
)
