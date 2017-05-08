# -*- coding: utf-8 -*-
"""
behave-profiles
"""
from setuptools import setup, find_packages
import os

HERE = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(HERE, 'README.rst')).read()

VERSION = '0.0.1'

setup(name='behave-profiles',
      version=VERSION,
      description="Reduce feature boilerplate defining testing profiles",
      long_description=README,
      classifiers=[
          'Development Status :: 4 - Beta',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Topic :: Software Development :: Testing'
      ],
      keywords='bdd testing behave metasteps',
      author='Roberto Abdelkader Martínez Pérez',
      author_email='robertomartinezp@gmail.com',
      url='https://github.com/buguroo/behave-profiles',
      license='LGPLv3',
      packages=["behave_profiles",
                "behave_profiles.steps",
                "behave_profiles.steps.stepcollection"],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
      ])
