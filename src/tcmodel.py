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
import datetime
import xmlrpclib

class TcGeneric(object):
    '''
    Parses data as a list of strings or an iterable
    and assigns the strings to class defined attribute names
    '''
    def __init__(self, data):
        for attrindex, attrname in enumerate(self.attrmap):
            field = data[attrindex]
            if isinstance(field, (basestring, bool, float, int,)):
                setattr(self, attrname, field)
            elif isinstance(field, xmlrpclib.DateTime):
                dt = datetime.datetime.strptime(field.value, "%Y%m%dT%H:%M:%S")
                setattr(self, attrname, dt)
            elif isinstance(field, dict):
                setattr(self, attrname, field)
                for name, value in field.iteritems():
                    setattr(self, name, value)
            elif isinstance(field, collections.Iterable):
                setattr(self, attrname, field)
                for elem in field:
                    setattr(self, elem[0], elem[1])
            else:
                raise TypeError('unknown type for TcGeneric %s in %s' % (str(field), str(data)))


class TestCatalog(TcGeneric):
    headers = [ 'Category', 'SubCategory', 'Test Case ID', 'Test Purpose', 'Design ID',
                'Prerequisites', 'Test Execution', 'Expected Results', 'Comments',]

    attrmap = ['id', 'page_name', 'title', 'description']

    def __init__(self, data=None):
        if not data:
            data = ['' for x in xrange(len(self.attrmap))]
        TcGeneric.__init__(self, data)


class TestCase(TcGeneric):
    attrmap = ['id', 'page_name', 'title', 'description']
    attdesc = ['purpose', 'cpeid', 'headline', 'prereq', 'execution', 'results', 'comments']

    def __init__(self, data):
        TcGeneric.__init__(self, data)

        self.tcid = self.title
        self.pdescription()
        
    def pdescription(self):
        lines = self.description.split('\n')
        self.description = list()

        curtxt = ''
        for line in lines:
            if line.startswith('=='):
                self.description.append(curtxt)
                curtxt = ''
            else:
                curtxt += line + '\n'

        # Add remainder or empty section
        self.description.append(curtxt)

        # Mapto names
        for idx, value in enumerate(self.description):
            setattr(self, self.attdesc[idx], value)
        
    def get_catalog_id(self):
        ''' Adapted from TestManagerFromTrac itself '''
        return self.page_name.rpartition('TT')[2].rpartition('_')[0]
        

class TestCaseInPlan(TcGeneric):
    statusmap = {'to_be_tested': 'To Be Tested',
                 'successful': 'Passed', 'passed': 'Passed',
                 'failed': 'Failed',
                 'skipped': 'Skipped', 'na': 'N/A',
                 'investigation': 'Investigation',}

    attrmap = ['id', 'page_name', 'status', 'title', 'timestamp', 'author', 'customfields',]

    def get_status(self):
        return self.statusmap[self.status]

class Ticket(TcGeneric):
    attrmap = ['id', 'created', 'changed', 'values',]
