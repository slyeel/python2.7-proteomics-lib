#!/bin/env python
#
# -*- coding: utf-8 -*-
#
# Copyright (C) University of Manchester 2012 
#               Julian Selley <j.selley@manchester.ac.uk>
################################################################################

"""
Mascot User example
===================
This is an example to show how to use the Mascot User file reader.

Description
-----------
This code shows the processes of loading the Mascot User file (an XML
file), and use the user information returned from the loading
procedure.

Take a look through the source code for detailed comments and the walk
through of the process.

When run, the code will generate the following output:
    $ python mascot_user_file.py 
    name: guest
    name: admin
    name: daemon
    name: (system)
    $ 
This is just a list of the user names in the supplied demo user file.

"""
# Metadata
__version__   = '0.1.0'
__author__    = 'Julian Selley <j.selley@manchester.ac.uk'
__copyright__ = 'Copyright 2011 Julian Selley <j.selley@manchester.ac.uk>'
__license__   = 'The Artistic License 2.0 (see the file LICENSE included with the distribution)'

# This is a bit of a *hack*
# to make this code work as part of the package.
from os.path import join as pjoin

# check .. for the mascot module to test.
import sys
sys.path.append(pjoin('..', '..'))

# Import the proteomics package.
import proteomics.mascot

# Create a file pointer, referencing a relative or absolute path to
# the Mascot User file.
# 
# In this example, we use os.path.join to make sure the code can be
# used in both UN*X and Windows environments alike (theoretically
# anyway).
usr_file_reader = proteomics.mascot.UserXMLInputFileReader(
    pjoin('..', 'tests', 'test_data', 'user.xml'))

# Read the Mascot User XML file into memory, and store it as an array
# of User objects (or struct's as C would define them, since they
# have no methods attached.
users = usr_file_reader.read_file()

# Cycle through the array of Group objects, and print each Group name
# to the screen.
for name in [user.username for user in users]:
    print "name: %s" % name
