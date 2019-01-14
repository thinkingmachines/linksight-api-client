# -*- coding: utf-8 -*-

# Import modules
from setuptools import find_packages, setup

with open('README.md', encoding='utf8') as readme_file:
    readme = readme_file.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

with open('requirements-dev.txt') as f:
    dev_requirements = f.read().splitlines()

setup(
    name='linksight-api-client',
    version='1.0.0',
    description='Python API client for LinkSight',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Thinking Machines Data Science',
    author_email='hello@thinkingmachin.es',
    url='https://github.com/thinkingmachines/linksight-api-client',
    packages=find_packages(exclude=['docs', 'tests']),
    include_package_data=True,
    install_requires=requirements,
    tests_require=dev_requirements,
    extras_require={'test': dev_requirements},
    license='GNU General Public License v2 (GPLv2)',
    zip_safe=False,
    keywords=['linksight', 'python client', 'geospatial'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Topic :: Scientific/Engineering',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.5',
    ],
)
