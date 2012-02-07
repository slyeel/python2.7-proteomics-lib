#!/bin/env python
#
# -*- coding: utf-8 -*-
#
# Copyright (C) University of Manchester 2011 
#               Julian Selley <j.selley@manchester.ac.uk>
################################################################################

"""
Proteomics package
==================
This package provides methodologies linked with Proteomics and Protein
Mass Spectrometry. This particular module simply loads the other
modules in the package.

Overview
--------

This package aims to provide methodologies for dealing with proteomics data. Currently, the only module part of this package is one connected with processing U{Matrix Science's Mascot <http://www.matrixscience.com/>} software data.

"""

# Metadata
__version__   = '0.1.0'
__author__    = 'Julian Selley <j.selley@manchester.ac.uk>'
__copyright__ = 'Copyright 2011 Julian Selley <j.selley@manchester.ac.uk>'
__license__   = 'The Artistic License 2.0 (see the file LICENSE included with the distribution)'

__all__ = [ "mascot" ]
