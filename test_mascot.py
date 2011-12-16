#!/bin/env python
#
# -*- coding: utf-8 -*-
#
# Copyright (C) University of Manchester 2011 
#               Julian Selley <j.selley@manchester.ac.uk>
################################################################################

"""
.. module:: test_mascot
    :platform: Unix
    :synopsis: A test module using unittest to test the Mascot module
.. moduleauthor: Julian Selley <j.selley@manchester.ac.uk>

Test Mascot Module
******************
This is a test suite for the Mascot module.

Overview
========

TODO 201112130955 JNS: write the documentation for this test suite

"""

# Metadata
__version__   = '0.01'
__author__    = 'Julian Selley <j.selley@manchester.ac.uk'
__copyright__ = 'Copyright 2011 Julian Selley <j.selley@manchester.ac.uk>'
__license__   = '''\
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
'''

# Imports
import mascot
import unittest

class TestGroupXMLInputFileReader(unittest.TestCase):
    def setUp(self):
        '''sets up a reader'''
        self.grp_reader = mascot.GroupXMLInputFileReader('test_data/group.xml')
        '''read the group file'''
        self.groups = self.grp_reader.read_file()

    def test_number_groups(self):
        '''check the number of groups is correct'''
        self.assertEqual(len(self.groups), 5,
                        'check the number of groups returned')

    def test_interrogate_groups(self):
        '''check the Guests group is in the group.xml file'''
        self.assertIn('Guests', [group.name for group in self.groups],
                        'check Guest group exists')

        '''check the guest group'''
        for group in self.groups:
            if (group.name != 'Guests'):
                continue

            self.assertNotEqual(group.id, '1', 'group id of guest')
            self.assertEqual(group.id, 1, 'group id of guest')

class TestLogInputFileReader(unittest.TestCase):
    def setUp(self):
        self.logs = []
        '''sets up a reader'''
        self.log_reader = mascot.LogInputFileReader('test_data/searches.log')
        '''store the logs in an list of LogEntry'''
        for log_entry in self.log_reader:
            try:
                self.logs.append(log_entry)
            except StopIteration:
                pass

    def test_number_log_entries(self):
        self.assertEqual(len(self.logs), 10, 'number of log entries')

    def test_search_ids(self):
        self.assertEqual([log.searchid for log in self.logs], range(1, 11),
                         'search ids')

    def test_ipaddr(self):
        self.assertEqual(''.join([log.ipaddr for log in self.logs]),
                         '130.88.0.0' * (len(self.logs) - 1),  # -1 because one of the log entries is missing an ipaddr
                         'IP address is 130.88.0.0')

class TestUserXMLInputFileReader(unittest.TestCase):
    def setUp(self):
        '''sets up a reader'''
        self.usr_reader = mascot.UserXMLInputFileReader('test_data/user.xml')
        '''read the user file'''
        self.users = self.usr_reader.read_file()

    def test_number_users(self):
        '''check the number of users is correct'''
        self.assertEqual(len(self.users), 4,
                        'check the number of users returned')

    def test_interrogate_users(self):
        '''check the guest user is in the user.xml file'''
        self.assertIn('guest', [user.username for user in self.users],
                        'check guest user exists')

        '''check the guest user'''
        for user in self.users:
            if (user.username != 'guest'):
                continue

            self.assertNotEqual(user.id, '1', 'user id of guest')
            self.assertEqual(user.id, 1, 'user id of guest')
            self.assertEqual(user.fullname, 'Guest user', 'full name of guest')
            self.assertEqual(user.email, 'guest@localhost',
                             'email address of guest')

if __name__ == '__main__':
    groupSuite = unittest.TestLoader().loadTestsFromTestCase(TestGroupXMLInputFileReader)
    logSuite   = unittest.TestLoader().loadTestsFromTestCase(TestLogInputFileReader)
    userSuite  = unittest.TestLoader().loadTestsFromTestCase(TestUserXMLInputFileReader)
    suite      = unittest.TestSuite([groupSuite, logSuite, userSuite])
    #suite = unittest.TestLoader().loadTestsFromModule('mascot_test.py')
    unittest.TextTestRunner(verbosity=2).run(suite)
