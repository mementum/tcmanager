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

import Queue
import threading
import urlparse
import xmlrpclib


class RpcThread(threading.Thread):

    def __init__(self, group=None, target=None, name=None, *args, **kwargs):
        threading.Thread(self, group=group, target=target, name=name, *args, **kwargs):
        self.q = Queue.PriorityQueue()

        self.url = ''
        self.username = ''
        self.password = ''


    def run(self):
        prio, data = self.q.get(block=True, timeout=None)

        if data is None:
            return # finishing

        method = getattr(self, data.reqmethod)
        method(data)


    def setUrl(self, baseurl, username, password):
        spliturl = baseurl.urlsplit()
        newsplit = list()
        for elem in baseurl.urlsplit():
            newsplit.append(elem)

        if self.username:
            prenetloc = self.username
            if self.password:
                prenetloc += ':%s' % self.password

            newsplit[1] = '%s@%s' % (prenetloc, newsplit[1])

        url =  urlparse.urlunsplit(newsplit)

        try:
            self.server = xmlrpclib.ServerProxy(url)
        except xmlrpclib.ProtocolError:
            wx.CallAfter() # signal the error
        except: xmlrpclib.Fault:
            wx.CallAfter() # signal the error

        wx.CallAfter() # indicate success


    def listRootCatalogs(self, data):
        try:
            self.server.testmanager.listSubCatalogs('-1'):
        except xmlrpclib.ProtocolError:
            wx.CallAfter() # signal the error
        except: xmlrpclib.Fault:
            wx.CallAfter() # signal the error

        wx.CallAfter() # indicate success

