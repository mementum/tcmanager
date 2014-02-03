#!/usr/bin/env python
# -*- coding: utf-8; py-indent-offset:4 -*-
################################################################################
# 
#   Copyright (C) 2014 Daniel Rodriguez
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

import datetime
import xmlrpclib

from tcmodel import Ticket
from rpcsupport import RpcInterface

class RpcSupport(object):

    def __init__(self, server, username, password):
        self.rpc = RpcInterface(server, username, password)

    def get_tickets(self, ticket_ids):
        multicall = self.rpc.multicall()
        for ticket_id in ticket_ids:
            multicall.ticket.get(ticket_id)

        return map(Ticket, multicall()) # list

    def get_tickets_by_id(self, ticket_ids):
        tickets = self.get_tickets(ticket_ids)
        return dict(map(lambda x: (x.id, x), tickets)) # dict indexed by ticket_id

    def update_tickets(self, ticket_updates):
        multicall = self.rpc.multicall()
        for ticket_update in ticket_updates:
            ticket_update = self.ticket_update_check(*ticket_update)
            print "ticket_update", ticket_update, 
            multicall.ticket.update(*ticket_update)
        multicall()

    def ticket_update_check(self, id, comment, attributes=None, notify=False, author='', when=None):
        print "ticket", id, comment, attributes, notify, author, when
        if not attributes:
            attributes = dict()
        if not when:
            when = datetime.datetime.now()
        when = xmlrpclib.DateTime(when)

        return id, comment, attributes, notify, author, when
