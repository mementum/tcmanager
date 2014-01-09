#!/usr/bin/env python
# -*- coding: latin-1; py-indent-offset:4 -*-
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

import collections

class TcGeneric(object):
    def __init__(self, data):
        for attrindex, attrname in enumerate(self.attrmap):
            # print data
            field = data[attrindex]
            if isinstance(field, basestring):
                setattr(self, attrname, field)
            elif isinstance(field, collections.Iterable):
                attr = list()
                setattr(self, attrname, attr)
                for elem in field:
                    attr.append(TcCustomFields(elem))
            else:
                raise TypeError('unknown type for TcGeneric %s in %s' % (str(field), str(data)))


class TcCustomFields(object):
    attrmap = ['name', 'value', 'label',]
    def __init__(self, data):
        for attrindex, attrname in enumerate(self.attrmap):
            setattr(self, attrname, data[attrindex])


class TestCaseInPlan(TcGeneric):
    attrmap = ['id', 'page_name', 'status', 'title', 'timestamp', 'author', 'customfields',]
