#!/bin/env python
#
# -*- coding: utf-8 -*-
#
# Copyright (C) University of Manchester 2011 
#               Julian Selley <j.selley@manchester.ac.uk>
################################################################################

"""
Enzyme module
=============
This module contains code related to enzyme digestion.

Description
-----------

Dependancies
------------

"""

# Metadata
__version__   = '1.0.1'
__author__    = 'Julian Selley <j.selley@manchester.ac.uk>'
__copyright__ = 'Copyright 2011 University of Manchester, Julian Selley <j.selley@manchester.ac.uk>'
__license__   = 'The Artistic License 2.0 (see the file LICENSE included with the distribution)'

# Imports
import abc
import logging;
import re

# Setup the logger
logger = logging.getLogger(__name__)

class abstractstatic(staticmethod):
    """Allows Abstract Static methods to be created.

    This is a neat trick defined and explained on
    http://stackoverflow.com/questions/4474395/staticmethod-and-abc-abstractmethod-will-it-blend.

    """
    __slots__ = ()
    def __init__(self, function):
        super(abstractstatic, self).__init__(function)
        function.__isabstractmethod__ = True

class DigestionEnzyme:
    """An abstract class, depicting a proteolytic enzyme.

    """
    __metaclass__ = abc.ABCMeta

    @abstractstatic
    def digest(sequence):
        """Digests a supplied protein sequence.

        """
        raise NotImplementedError

class Trypsin(DigestionEnzyme):
    """Mimics Trypsin digestion of protein sequences.

    """
    @staticmethod
    def digest(sequence):
        """Digests a protein sequence as Trypsin theoretically does.

        """
        return re.sub('(?<=[KR])(?=[^P])', '\n', sequence.upper()).split()

#if __name__ == '__main__':
#    logging.basicConfig(level=logging.DEBUG)
#    
