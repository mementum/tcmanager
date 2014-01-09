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

import wx

def ConfigPrefix(cfgprefix):
    def ClassWrapper(cls):
        cls._cfgprefix = cfgprefix
        return cls
    return ClassWrapper

class ConfigItem(object):
    def __init__(self, name, defvalue):
        self.name = name
        # Will be created on demand. Absence (AttributeError) signals
        # it has not yet been set
        # self.icache = None
        self.defvalue = defvalue

    def getname(self, instance):
        if hasattr(instance, '_cfgprefix'):
            return '%s/%s' % (instance._cfgprefix, self.name)
        return self.name

    def __get__(self, instance, owner=None):
        try:
            return self.icache
        except AttributeError:
            retval = self.rd(self.getname(instance), self.defvalue)
            self.config.Flush() # in case defvalue has been used
            self.icache = retval
            return retval
            
    def __set__(self, instance, value):
        try:
            if self.icache == value:
                return
        except AttributeError:
            pass

        self.icache = value
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
