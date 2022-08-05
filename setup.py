#!/usr/bin/env python

from setuptools import setup

requirements = []  # add Python dependencies here
# e.g., requirements = ["PyYAML"]

setup(
    name='awx-passwordstate-credential-plugin',
    version='0.1',
    author='R. van Dongen',
    author_email='info@qonnect-it.nl',
    description='Passwordstate compatible credential plugin',
    long_description='',
    license='Apache License 2.0',
    keywords='ansible',
    url='https://github.com/royvandongen/awx-passwordstate-credential-plugin',
    packages=['awx_passwordstate_credential_plugin'],
    include_package_data=True,
    zip_safe=False,
    setup_requires=[],
    install_requires=requirements,
    entry_points = {
        'awx.credential_plugins': [
            'passwordstate_plugin = awx_passwordstate_credential_plugin:passwordstate_plugin',
        ]
    }
)
