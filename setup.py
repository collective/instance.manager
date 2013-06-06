from setuptools import setup, find_packages
import os

version = '0.0.1'

long_description = (
    open('README.rst').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.rst').read()
    + '\n' +
    open('CHANGES.rst').read()
    + '\n')

setup(name='instance.manager',
      version=version,
      description="Desktop applet used to manage Plone Sites",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='Rodrigo Ferreira de Souza',
      author_email='rodfersou at gmail dot com',
      url='https://github.com/collective/instance.manager',
      license='gpl',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['instance'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'PySide==1.1.2',
      ],
      scripts=['bin/instancemanager'],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
