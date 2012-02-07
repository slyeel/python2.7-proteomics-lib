#!/usr/bin/env python
#
# -*- coding: utf-8 -*-
#
# Copyright (C) University of Manchester 2011 
#               Julian Selley <j.selley@manchester.ac.uk>
################################################################################

"""
Proteomics module setup
=======================
This module setup's the package for installation -- it implements the distutils
of python.

"""

# Metadata
__version__ = '0.1.0'
__author__  = 'Julian Selley <j.selley@manchester.ac.uk>'
__copyright__ = 'Copyright 2012 University of Manchester, Julian Selley <j.selley@manchester.ac.uk>'
__license__   = 'The Artistic License 2.0 (see the file LICENSE included with the distribution)'

# Imports
from __init__ import __version__
from distutils.core import setup, Command
from unittest import TextTestRunner, TestLoader
from glob import glob
from os.path import splitext, basename, join as pjoin, walk
import os

class TestCommand(Command):
    user_options = [ ]

    def initialize_options(self):
        self._dir = os.getcwd()

    def finalize_options(self):
        pass

    def run(self):
        '''
        Finds all the tests modules in tests/, and runs them.
        '''
        testfiles = [ ]
        for t in glob(pjoin(self._dir, 'tests', '*.py')):
            if not t.endswith('__init__.py'):
                testfiles.append('.'.join(
                    ['tests', splitext(basename(t))[0]])
                )

        tests = TestLoader().loadTestsFromNames(testfiles)
        t = TextTestRunner(verbosity = 1)
        t.run(tests)

class CleanCommand(Command):
    user_options = [ ]

    def initialize_options(self):
        self._clean_me = [ ]
        for root, dirs, files in os.walk('.'):
            for f in files:
                if f.endswith('.pyc'):
                    self._clean_me.append(pjoin(root, f))

    def finalize_options(self):
        pass

    def run(self):
        for clean_me in self._clean_me:
            try:
                os.unlink(clean_me)
            except:
                pass

setup(name = 'proteomics',
      version = __version__,
      description = 'A library of Proteomic class and methods',
      long_description = 'A library of Proteomic class and methods',
      author = 'Julian Selley',
      author_email = 'j.selley@manchester.ac.uk',
      maintainer = 'Julian Selley',
      maintainer_email = 'j.selley@manchester.ac.uk',
      url = 'http://fls-bioinformatics-core.github.com/proteomics-python2.7-proteomics-lib/',
      license = 'The Artistic License 2.0',
      #install_requires = [],
      classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Artistic License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Chemistry',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      packages = ['proteomics'],
      package_dir = {'proteomics' : '.'},
      package_data = {'' : ['README.md', 'CHANGES', 'epydoc.conf', 'LICENSE', 'INSTALL']},
      #data_files = [('config', ['epydoc.conf']),],
      cmdclass = {'test': TestCommand, 'clean': CleanCommand},
      #entry_points = {'' : [''],},
)

# patch distutils if it can't cope with the "classifiers" or
# "download_url" keywords
from sys import version
if version < '2.2.3':
    from distutils.dist import DistributionMetadata
    DistributionMetadata.classifiers = None
    DistributionMetadata.download_url = None
