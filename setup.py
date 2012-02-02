#!/usr/bin/env python
#
# -*- coding: utf-8 -*-
#
# Copyright (C) University of Manchester 2011 
#               Julian Selley <j.selley@manchester.ac.uk>
################################################################################

__docformat__ = 'restructuredtext en'

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
from distutils.core import setup

setup(name = 'proteomics',
      version = proteomics.__version__,
      description = 'A library of Proteomic class and methods',
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
)

# patch distutils if it can't cope with the "classifiers" or
# "download_url" keywords
from sys import version
if version < '2.2.3':
    from distutils.dist import DistributionMetadata
    DistributionMetadata.classifiers = None
    DistributionMetadata.download_url = None
