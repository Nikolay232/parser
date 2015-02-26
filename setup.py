#!/usr/bin/env python
import sys

from setuptools import setup, find_packages

if sys.argv[1] == 'develop':
    import multiprocessing
else:
    pass


requires = [
    'Pillow < 2.4',
    'django < 1.7',
    'configobj',
    'psycopg2 < 2.6',
    'django-admin-tools',
    'graypy'
]


dependencies = [
    #'https://github.com/hhru/pika/tarball/0.9#egg=pika-0.9.6-pre0',
    #'https://github.com/hhru/lucid-python-django-admin-tools/tarball/EWD-1391#egg=django-admin-tools-0.5.1-hh2',
    'https://github.com/Nikolay232/inmemorystorage/tarball/six_1.5#egg=dj-inmemorystorage-1.0.1'
]

setup(
    name='parser',
    version='0.1',
    description='parser',
    keywords='web django parser',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    zip_safe=False,
    include_package_data=True,
    author='niko',
    dependency_links=dependencies,
    install_requires=requires,
    extras_require={
        'dev': [
            'PyYAML == 3.10',
            'dj-inmemorystorage'
        ]},
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Framework :: Django",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
    ],
    entry_points={
        'console_scripts': [
            'parser = parser.manage:main',
        ]
    }
)
