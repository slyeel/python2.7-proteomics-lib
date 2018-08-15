#!/bin/env python
#
# -*- coding: utf-8 -*-
#
# Copyright (C) University of Manchester 2012 
#               Julian Selley <j.selley@manchester.ac.uk>
################################################################################

"""
Test Enzyme Module
******************
This is a test suite for the enzyme module. It tests the elements of the enzyme
module.

Overview
========

@todo 201112130955 JNS: write the documentation for this test suite

"""

# Metadata
__version__   = '0.1.0'
__author__    = 'Julian Selley <j.selley@manchester.ac.uk'
__copyright__ = 'Copyright 2011 Julian Selley <j.selley@manchester.ac.uk>'
__license__   = 'The Artistic License 2.0 (see the file LICENSE included with the distribution)'

# This is a bit of a *hack*
# to make this code work as part of the package.
from os.path import join as pjoin

# check ../.. for the mascot module to test
import sys
sys.path.append(pjoin('..', '..'))

# Imports
import proteomics.enzyme
import unittest

# There is no test for the struct classes as these simply store data, without
# any methods attached to test.

class DigestionEnzymeTestCase(unittest.TestCase):
    """Provides a template for testing DigestionEnzyme sub-classes.

    The DigestionEnzyme class is an abstract class, so it should throw
    a NotImplemented exception. This is the one test that this class
    checks.

    """
    def setUp(self):
        """Sets up the group of tests for DigestionEnzyme.

        However, this is an abstract class that should throw an
        NotImplemented exception if an instance is tried to be
        generated.

        """
        self.sequence = ''.join(
            ["MAGKKGQKKSGLGNHGKNSDMDVEDRLQAVVLTDSYETRFMPLTAVKPRCLLPLANVPLI",
             "EYTLEFLAKAGVHEVFLICSSHANQINDYIENSKWNLPWSPFKITTIMSPEARCTGDVMR"])

    def test_abstract_static_digest(self):
        """Checks this class is abstract.

        If you try and create a DigestionEnzyme, which is an abstract
        class, it should throw a NotImplemented exception.

        """
        with self.assertRaises(NotImplementedError) as cm:
            proteomics.enzyme.DigestionEnzyme.digest(self.sequence)

class TrypsinTestCase(DigestionEnzymeTestCase):
    """Test the Trypsin class.

    This set of tests check the DigestionEnzyme Trypsin.

    """
    def setUp(self):
        """Sets up the group of tests.

        It does this by providing a definition of the expected
        digestion of the sequence provided in DigestionEnzymeTestCase,
        which this TestCase extends.

        """
        super(TrypsinTestCase, self).setUp()
        self.expected_peptides = ["MAGK",
                                  "K",
                                  "GQK",
                                  "K",
                                  "SGLGNHGK",
                                  "NSDMDVEDR",
                                  "LQAVVLTDSYETR",
                                  "FMPLTAVKPR",
                                  "CLLPLANVPLIEYTLEFLAK",
                                  "AGVHEVFLICSSHANQINDYIENSK",
                                  "WNLPWSPFK",
                                  "ITTIMSPEAR",
                                  "CTGDVMR"]
        self.observed_peptides = proteomics.enzyme.Trypsin.digest(self.sequence)

    def test_trypsin_digestion(self):
        """Checks the digestion by the Trypsin DigestionEnzyme.

        Checks that the function digest, produces the expected
        output.

        """
        self.assertEqual(len(self.observed_peptides),
                         len(self.expected_peptides),
                         'check the length of digested peptides')
        self.assertEqual(self.observed_peptides,
                         self.expected_peptides,
                        'check all elements are equal')

# if this test is being run from the command line, generate the relevant suites,
# combine them together and then run them.
if __name__ == '__main__':
    deSuite = unittest.TestLoader().loadTestsFromTestCase(DigestionEnzymeTestCase)
    trypsinSuite   = unittest.TestLoader().loadTestsFromTestCase(TrypsinTestCase)
    suite      = unittest.TestSuite([deSuite, trypsinSuite])
    #suite = unittest.TestLoader().loadTestsFromModule('enzyme_test.py')
    unittest.TextTestRunner(verbosity=2).run(suite)
