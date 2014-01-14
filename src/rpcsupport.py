#!/usr/bin/env python
# -*- coding: latin-1; py-indent-offset:4 -*-
################################################################################
# 
#   Copyright (C) 2013 Daniel Rodriguez
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
################################################################################

import urlparse
import xmlrpclib


class RpcInterface(object):

    def __init__(self, baseurl, username, password):
        self.SetServer(baseurl, username, password)

    def SetServer(self, baseurl, username, password):
        if baseurl[-1] != '/':
            baseurl += '/'
        baseurl += 'login/xmlrpc'
        spliturl = urlparse.urlsplit(baseurl)
        newsplit = list()
        for elem in spliturl:
            newsplit.append(elem)

        if username:
            prenetloc = username
            if password:
                prenetloc += ':%s' % password

            newsplit[1] = '%s@%s' % (prenetloc, newsplit[1])

        self.url = urlparse.urlunsplit(newsplit)
        self.server = xmlrpclib.ServerProxy(self.url)

    def listSubCatalogs(self, catid):
        '''
        Returns a list of subcatalogs of "catid". Use -1 to list the catalogs from the root.

        Each catalog is also a list (all text fields): [id, internal_text_id, title, description]
        
        The internal_text_id looks like:
          TC_TTId and recursively for further subcatalogs TC_TTId_TTSubId
        '''
        return self.server.testmanager.listSubCatalogs(catid)

    def listSubCatalogsExt(self, catid=''):
        '''
        Returns a list of subcatalogs of "catid". Use -1 to list the catalogs from the root.

        Each catalog is also a list (all text fields): [id, internal_text_id, title, description]
        
        The internal_text_id looks like:
          TC_TTId and recursively for further subcatalogs TC_TTId_TTSubId
        '''
        return self.server.testmanager.listSubCatalogsExt(catid)

    def createTestCatalog(self, catid, name, description):
        return self.server.testmanager.createTestCatalog(catid, name, description)

    def createTestCase(self, catid, title, description):
        return self.server.testmanager.createTestCase(catid, title, description)

    def deleteTestCatalog(self, catid):
        return self.server.testmanager.deleteTestObject('testcatalog', catid)

    def getTestCatalog(self, catid):
        return self.server.testmanager.getTestCatalog(catid)

    def listTestCases(self, catid, plan_id=''):
        return self.server.testmanager.listTestCases(catid, plan_id)

    def listTestPlans(self, catid):
        return self.server.testmanager.listTestPlans(catid)

    def listTestCasesExt(self, catid, plan_id='', deep=False):
        return self.server.testmanager.listTestCasesExt(catid, plan_id, deep)
