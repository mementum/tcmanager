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
import cPickle

import wx

def ConfigPrefix(cfgprefix):
    def ClassWrapper(cls):
        cls._cfgprefix = cfgprefix
        return cls
    return ClassWrapper

class ConfigItem(object):
    def __init__(self, name, defvalue):
        self.name = name
        self.icache = dict()
        # Defvalue will be passed through postrd
        # if returned because no value is in the cache
        # and therefore we need to keep it like if it
        # was the value we wrote down to the registry
        # or config file
        self.defvalue = self.prewr(defvalue)

    def getname(self, instance):
        if hasattr(instance, '_cfgprefix'):
            return '%s/%s' % (instance._cfgprefix, self.name)
        return self.name

    def postrd(self, value):
        return value

    def prewr(self, value):
        return value

    def __get__(self, instance, owner=None):
        try:
            return self.icache[instance]
        except KeyError:
            retval = self.rd(self.getname(instance), self.defvalue)
            self.config.Flush() # in case defvalue has been used
            retval = self.postrd(retval)
            self.icache[instance] = retval
            return retval
            
    def __set__(self, instance, value):
        try:
            if self.icache[instance] == value:
                return # avoid writing to files/registry
        except KeyError:
            pass

        self.icache[instance] = value
        value = self.prewr(value)
        self.wr(self.getname(instance), value)
        self.config.Flush()

    @property
    def config(self):
        return wx.Config.Get()

    @property
    def wr(self):
        return getattr(self.config, self.wrattr)

    @property
    def rd(self):
        return getattr(self.config, self.rdattr)

class ConfigString(ConfigItem):
    wrattr = 'Write'
    rdattr = 'Read'

class ConfigBool(ConfigItem):
    wrattr = 'WriteBool'
    rdattr = 'ReadBool'

class ConfigInt(ConfigItem):
    wrattr = 'WriteInt'
    rdattr = 'ReadInt'

class ConfigFloat(ConfigItem):
    wrattr = 'WriteFloat'
    rdattr = 'ReadFloat'

class ConfigList(ConfigString):
    def __init__(self, name, defvalue=[]):
        # No problem with default value [] because
        # it's going to be pickled in the constructors
        # parent and the result is a string which
        # is no longer the memoized string
        ConfigString.__init__(self, name, defvalue)
        
    def postrd(self, value):
        # Do a str conversion because wx.config returns a unicode string
        # but the pickle protocol uses ascii
        retval = cPickle.loads(str(value))
        if retval is None:
            retval = list()
        return retval

    def prewr(self, value):
        return cPickle.dumps(value)
        
            
