"""Setup."""
# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

setup(
    name='tap-twinfield',
    version='0.1.0',
    description='Singer.io tap for extracting data from Twinfield',
    author='Stitch',
    url='https://github.com/Yoast/singer-tap-twinfield',
    classifiers=['Programming Language :: Python :: 3 :: Only'],
    py_modules=['tap_adyen'],
    install_requires=[
        'defusedxml~=0.6.0',
        'lxml~=4.6.2',
        'pandas~=1.2.2',
        'python-dateutil~=2.8.1',
        'singer-python~=5.10.0',
        'zeep~=4.0.0',
    ],
    entry_points="""
        [console_scripts]
        tap-twinfield=tap_twinfield:main
    """,
    packages=find_packages(),
    package_data={
        'tap_twinfield': [
            'schemas/*.json',
        ],
    },
    include_package_data=True,
)
