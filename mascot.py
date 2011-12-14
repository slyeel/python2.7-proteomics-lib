# Copyright 2011 Julian Selley <j.selley@manchester.ac.uk>

'''
This module contains information related to interpreting Mascot information

Overview
========

TODO 201111180955 JNS: write the documentation for this library
'''

# metadata
__version__   = '0.01'
__author__    = 'Julian Selley <j.selley@manchester.ac.uk>'
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

# imports
import csv
import logging
import xml.dom.minidom

# setup the logger
logger = logging.getLogger('mascot')

class Group:
    id   = None
    name = None
    uids = []

class GroupXMLInputFileReader:
    '''This class represents the Mascot group file, and allows for querying
    the data contained therein'''

    def __init__(self, filename = 'data/group.xml'):
        self._filename = filename

    # TODO 20111119 JNS: document function ???
    def read_file(self):
        _grps = []
        __group_doc = xml.dom.minidom.parse(self._filename)  # the group DOM
        __grp = None  # a representation (struct) of a group
        # for each "mss:group_data" node in the XML
        for node in __group_doc.getElementsByTagName('mss:group_data'):
            # get every child node
            for childNode in node.childNodes:
                # go to the next node if it isn't an ELEMENT_NODE and isn't one
                # the specific informaiton of interest relating to groups
                if (childNode.nodeType != childNode.ELEMENT_NODE and 
                    childNode.localName != 'group_id' and
                    childNode.localName != 'group_name' and
                    childNode.localName != 'users'):
                    continue

                # if the node is about the group id
                if childNode.localName == 'group_id':
                    # if there was a previous group information, store it in
                    # the object
                    if (__grp != None):
                        _grps.append(__grp)
                        logger.debug("gid {0} stored".format(__grp.id))
                    # create a new group and store the group id
                    __grp = Group()
                    __grp.id = int(childNode.childNodes[0].data)
                    logger.debug("setting gid: %s",
                                 childNode.childNodes[0].data)
                # elif the node is the group name, set the group name
                elif childNode.localName == 'group_name':
                    __grp.name = childNode.childNodes[0].data
                    logger.debug("(gid: %s) name defined: %s",
                                 __grp.id, childNode.childNodes[0].data)
                # elif the node is about the associated users
                elif childNode.localName == 'users':
                    # get all the user childNodes ("mss:user_id"), and store the
                    # uid's
                    for user in childNode.childNodes:
                        if user.nodeType == user.ELEMENT_NODE and user.localName == "user_id":
                            __grp.uids.append(user.childNodes[0].data)
                            logger.debug("(gid: %s) uid added: %s",
                                         __grp.id, user.childNodes[0].data)
        # store the last group
        _grps.append(__grp)
        logger.debug("gid {0} stored".format(__grp.id))

        # return the users read in
        return _grps

class LogEntry:
    '''A log entry (a row) from the Mascot Log file, represented with each
    column'''
    searchid   = None
    pid        = None
    database   = None
    username   = None
    useremail  = None
    title      = None
    filename   = None
    start      = None
    duration   = None
    status     = None
    priority   = None
    searchtype = None
    enzyme     = None
    ipaddr     = None
    uid        = None

class LogInputFileReader:
    '''Mascot log reader'''
    def __init__(self, filename = 'data/logs/searches.log'):
        self._rows = []
        self._len = 0
        self._rowi = 0
        file = open(filename, 'rb')
        _csv = csv.reader(file, delimiter = '\t')
        for _row in _csv:
            self._rows.append(_row)
            self._len += 1
        file.close()

    def __len__(self):
        return self._len

    def __iter__(self):
        return self
    def next(self):
        if self._rowi >= len(self):
            raise StopIteration
        _logentry = LogEntry()
        # TODO 20111214 JNS: put in checks of data, with exceptions
        _logentry.searchid   = self._rows[self._rowi][0]
        _logentry.pid        = self._rows[self._rowi][1]
        _logentry.database   = self._rows[self._rowi][2]
        _logentry.username   = self._rows[self._rowi][3]
        _logentry.useremail  = self._rows[self._rowi][4]
        _logentry.title      = self._rows[self._rowi][5]
        _logentry.filename   = self._rows[self._rowi][6]
        _logentry.start      = self._rows[self._rowi][7]
        _logentry.duration   = self._rows[self._rowi][8]
        _logentry.status     = self._rows[self._rowi][9]
        _logentry.priority   = self._rows[self._rowi][10]
        _logentry.searchtype = self._rows[self._rowi][11]
        _logentry.enzyme     = self._rows[self._rowi][12]
        _logentry.ipaddr     = self._rows[self._rowi][13]
        _logentry.uid        = self._rows[self._rowi][14]
        self._rowi += 1

        return _logentry

class User:
    id       = None
    username = None
    fullname = None
    email    = None

class UserXMLInputFileReader:
    '''This class represents the Mascot user file, and allows for querying
    the data contained therein'''

    def __init__(self, filename = 'data/user.xml'):
        self._filename = filename

    # TODO 20111119 JNS: document function ???
    def read_file(self):
        _usrs = []
        __user_doc = xml.dom.minidom.parse(self._filename)  # the user DOM
        __usr = None  # a representation (struct) of a user

        # for each "mss:user_data" node in the XML
        for node in __user_doc.getElementsByTagName('mss:user_data'):
            # get every child node
            for childNode in node.childNodes:
                # go to the next node if it isn't an ELEMENT_NODE and isn't one
                # the specific informaiton of interest relating to userss
                if (childNode.nodeType != childNode.ELEMENT_NODE and 
                    childNode.localName != 'userID' and
                    childNode.localName != 'userName' and
                    childNode.localName != 'fullName' and
                    childNode.localName != 'emailAddress'):
                    continue

                # if the node is about the user id
                if childNode.localName == 'userID':
                    # if there was a previous user information, store it in
                    # the object
                    if (__usr != None):
                        _usrs.append(__usr)
                        logger.debug("uid {0} stored".format(__usr.id))
                    # create a new user and store the user id
                    __usr = User()
                    __usr.id = int(childNode.childNodes[0].data)
                    logger.debug("setting uid: %s",
                                 childNode.childNodes[0].data)
                # elif the node is the user name, set the user name
                elif childNode.localName == 'userName':
                    __usr.username = childNode.childNodes[0].data
                    logger.debug("(uid: %s) name defined: %s",
                                 __usr.id, childNode.childNodes[0].data)
                # elif the node is the full name, set the user's full name
                elif childNode.localName == 'fullName':
                    __usr.fullname = childNode.childNodes[0].data
                    logger.debug("(uid: %s) fullname defined: %s",
                                 __usr.id, childNode.childNodes[0].data)
                # elif the node is the email address, set the user's e-mail
                elif childNode.localName == 'emailAddress':
                    try:
                        __usr.email = childNode.childNodes[0].data
                        logger.debug("(uid: %s) email defined: %s",
                                     __usr.id, childNode.childNodes[0].data)
                    except IndexError:
                        pass
        # store the last user
        _usrs.append(__usr)
        logger.debug("uid {0} stored".format(__usr.id))

        # return the users read in
        return _usrs

#if __name__ == '__main__':
#    logging.basicConfig(level=logging.DEBUG)
#    group_f = GroupXMLInputFileReader()
#    groups = group_f.read_file()
#    if 'Hubbard' in [group.name for group in groups]:
#        print "hello"
#        user_f = UserXMLInputFileReader()
#        users = user_f.readFile()
#        if 'mjfssjs' in [user.username for user in users]:
#            print "hello"
