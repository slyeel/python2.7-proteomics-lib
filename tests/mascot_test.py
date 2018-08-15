#!/bin/env python
#
# -*- coding: utf-8 -*-
#
# Copyright (C) University of Manchester 2011 
#               Julian Selley <j.selley@manchester.ac.uk>
################################################################################

"""
Test Mascot Module
******************
This is a test suite for the Mascot module. It tests the elements of the Mascot
module, including various file readers / streams.

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
import proteomics.mascot
import unittest

# There is no test for the struct classes as these simply store data, without
# any methods attached to test.

class GroupXMLInputFileReaderTestCase(unittest.TestCase):
    """Test the Mascot Group XML File reader.

    This set of tests check the functionality of the Mascot Group XML File
    reader. The reader works as a reader, rather than streaming the file: this
    is because it is an XML file.

    """
    def setUp(self):
        """Sets up the group of tests by creating a Group File Reader object,
        and reading the file.

        It stores the groups in a variable contained in the object, for testing
        in the various tests.

        """
        # create a reference to the file reader.
        # use the Mascot Group XML File in the 'test_data' folder.
        self.grp_reader = proteomics.mascot.GroupXMLInputFileReader(pjoin('test_data', 'group.xml'))
        # read the file and store the list of groups in the test object
        self.groups = self.grp_reader.read_file()

    def test_number_groups(self):
        """Check the number of groups loaded from the test_data Group XML File.

        There should be 5 groups contained in the 'test_data' Mascot Group XML
        File.

        """
        self.assertEqual(len(self.groups), 5,
                        'check the number of groups returned')

    def test_interrogate_groups(self):
        """Check the groups contain the Guest group, and then interrogate that
        group.

        Check that the 'Guests' group is defined.

        """
        self.assertIn('Guests', [group.name for group in self.groups],
                        'check Guest group exists')

        """Identify the Guests group and make sure it's ID is 1.

        Check that the Group ID is also defined as an integer and not as a str.

        """
        for group in self.groups:
            if (group.name != 'Guests'):
                continue

            self.assertNotEqual(group.id, '1', 'group id of guest')
            self.assertEqual(group.id, 1, 'group id of guest')

class LogInputFileReaderTestCase(unittest.TestCase):
    """Test the Mascot log file reader.

    This set of tests check the functionality of the Mascot Log File reader.
    The reader works as a stream reader, rather than reading the data all in
    one go. It does however, open the file and read it's entire contents into
    memory. It only streams in terms of the way that data is passed back through
    the API.

    """
    def setUp(self):
        """Sets up the group of tests by creating a log file reader object, and
        reading the file.

        """
        # sets up a list of logs
        self.logs = []
        # create a reference to the file reader.
        # use the Mascot Log File in the 'test_data' folder.
        self.log_reader = proteomics.mascot.LogInputFileReader(pjoin('test_data', 'searches.log'))
        # store the logs in a list of LogEntry
        for log_entry in self.log_reader:
            try:
                self.logs.append(log_entry)
            except StopIteration:
                pass

    def test_number_log_entries(self):
        """Check the number of log entries loaded from the test_data search log
        file.

        There should be 10 log entries contained in the 'test_data' Mascot Log
        File.

        """
        self.assertEqual(len(self.logs), 10, 'number of log entries')

    def test_search_ids(self):
        """Check the ID's in the search log file.

        The search log file has been setup with sequential log ID's, from 1 to
        10. Check this is the case.

        """
        self.assertEqual([log.searchid for log in self.logs], range(1, 11),
                         'search ids')

    def test_ipaddr(self):
        """Check the IP addresses.

        For security purposes, the IP addresses have been changed to the wider
        B-class domain. Check that the IP addresses are correct, and that
        (because one entry is missing an IP address because it is actually a
        server submitted search to test the database), that there is one short
        of the 10 search log entries.

        """
        self.assertEqual(''.join([log.ipaddr for log in self.logs]),
                         '130.88.0.0' * (len(self.logs) - 1),  # -1 because one of the log entries is missing an ipaddr
                         'IP address is 130.88.0.0')

    """
    @todo: 20111220 JNS: test read_file
    @todo: 20111220 JNS: test reset
    """

class UserXMLInputFileReaderTestCase(unittest.TestCase):
    """Test the Mascot User XML File reader.

    This set of tests check the functionality of the Mascot User XML File
    reader. The reader works as a reader, rather than streaming the file: this
    is because it is an XML file.

    """
    def setUp(self):
        """Sets up the group of tests by creating a User File Reader object, and
        reading the file.

        It stores the users in a variable contained in the object, for testing
        in the various tests.

        """
        # create a reference to the file reader.
        # use the Mascot User XML File in the 'test_data' folder.
        self.usr_reader = proteomics.mascot.UserXMLInputFileReader(pjoin('test_data', 'user.xml'))
        # read the file and store the list of groups in the test object
        self.users = self.usr_reader.read_file()

    def test_number_users(self):
        """Check the number of groups loaded from the test_data User XML File.

        There should be 5 groups contained in the 'test_data' Mascot User XML
        File.

        """
        self.assertEqual(len(self.users), 4,
                        'check the number of users returned')

    def test_interrogate_users(self):
        """Check the users contain the guest user, and then interrogate that
        user.

        Check that the 'guest' user is defined.

        """
        self.assertIn('guest', [user.username for user in self.users],
                        'check guest user exists')

        """Identify the guest user and make sure it's ID is 1.

        Check that the guest ID is also defined as an integer and not as a str.
        Check the fullname of the guest user, and the e-mail address.

        """
        for user in self.users:
            if (user.username != 'guest'):
                continue

            self.assertNotEqual(user.id, '1', 'user id of guest')
            self.assertEqual(user.id, 1, 'user id of guest')
            self.assertEqual(user.fullname, 'Guest user', 'full name of guest')
            self.assertEqual(user.email, 'guest@localhost',
                             'email address of guest')

# if this test is being run from the command line, generate the relevant suites,
# combine them together and then run them.
if __name__ == '__main__':
    groupSuite = unittest.TestLoader().loadTestsFromTestCase(GroupXMLInputFileReaderTestCase)
    logSuite   = unittest.TestLoader().loadTestsFromTestCase(LogInputFileReaderTestCase)
    userSuite  = unittest.TestLoader().loadTestsFromTestCase(UserXMLInputFileReaderTestCase)
    suite      = unittest.TestSuite([groupSuite, logSuite, userSuite])
    #suite = unittest.TestLoader().loadTestsFromModule('mascot_test.py')
    unittest.TextTestRunner(verbosity=2).run(suite)
