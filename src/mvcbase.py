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
import functools
import inspect
import threading
import weakref

from pubsub import pub
import wx

class MvcAttribute(object):
    _mvccontainer = weakref.WeakValueDictionary()

    def __init__(self):
        self.icache = dict()

    def __set__(self, instance, value):
        self.icache[instance] = value

    def __get__(self, instance, owner=None):
        return self.icache.setdefault(instance)

def MvcContainer(cls):
    cls._model = MvcAttribute()
    cls._view = MvcAttribute()
    cls._controller = MvcAttribute()

    cls.__oldinit__ = cls.__init__

    @functools.wraps(cls.__init__)
    def newInit(self, *args, **kwargs):
        curThId = threading.current_thread().ident
        MvcAttribute._mvccontainer[curThId] = self
        self.__oldinit__(*args, **kwargs)

    cls.__init__ = newInit
    return cls

def MvcRole(role):
    def wrapper(cls):
        pubsubmap = {'view': 'model', 'controller': 'view'}

        oldInit = cls.__init__

        @functools.wraps(cls.__init__)
        def newInit(self, *args, **kwargs):
            # Assign the role
            self.role = role

            # Assign the mvcontainer
            curThId = threading.current_thread().ident
            self._mvccontainer = _mvccontainer = MvcAttribute._mvccontainer[curThId]

            # Pubsub some methods
            methods = inspect.getmembers(self.__class__, predicate=inspect.ismethod)
            mvcid = id(_mvccontainer)
            for method in methods:
                if hasattr(method[1], '_pubsub'):
                    boundmethod = method[1].__get__(self, self.__class__)
                    psmap = pubsubmap[role]
                    pstopic = '%d.%s.%s' % (mvcid, psmap, method[1]._pubsub)
                    pub.subscribe(boundmethod, pstopic)
                elif hasattr(method[1], '_pubsubspec'):
                    boundmethod = method[1].__get__(self, self.__class__)
                    pstopic = '%d.%s' % (mvcid, method[1]._pubsubspec)
                    pub.subscribe(boundmethod, pstopic)

            if role == 'view':
                # Rebind some methods to controller
                _controller = _mvccontainer._controller
                methods = inspect.getmembers(_controller, predicate=inspect.ismethod)
                for method in methods:
                    if hasattr(method[1], '_viewcontroller'):
                        setattr(self, method[0], method[1].__get__(self, self.__class__))

            oldInit(self, *args, **kwargs)

        cls.__init__ = newInit

        oldGetAttribute = cls.__getattribute__
        def newGetAttribute(self, name):
            _mvcroles = ['_model', '_view', '_controller']
            if name in _mvcroles:
                _mvccontainer = oldGetAttribute(self, '_mvccontainer')
                return getattr(_mvccontainer, name)

            return oldGetAttribute(self, name)
        cls.__getattribute__ = newGetAttribute

        if False:
            def PubSend(self, **kwargs):
                pub.sendMessage(self.role, **kwargs)

            cls.PubSend = PubSend
        
        return cls
    return wrapper

ModelRole = MvcRole('model')
ViewRole = MvcRole('view')
ControllerRole = MvcRole('controller')

def ViewManager(func):
    @functools.wraps(func)
    def wrapper(self, event, *args, **kwargs):
        event.Skip()
        return func(self, event, *args, **kwargs)

    wrapper._viewcontroller = True
    return wrapper

def PubSubscribe(subtopic):
    def decorate(func):
        func._pubsub = subtopic
        return func

    return decorate

def PubSubscribeSpecific(subtopic):
    def decorate(func):
        func._pubsubspec = subtopic
        return func

    return decorate

def PubSend(topic=None, queue=True):
    def decorate(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            mvcid = id(self._mvccontainer)
            try:
                msg = func(self, *args, **kwargs)
                if not topic:
                    sendtopic = None
                else:
                    sendtopic = '%d.%s.%s' % (mvcid, self.role, topic)
            except Exception, e:
                msg = str(e)
                sendtopic = '%d.%s.%s' % (mvcid, self.role, 'error')

            if sendtopic:
                if queue:
                    wx.CallAfter(pub.sendMessage, sendtopic, msg=msg)
                else:
                    pub.sendMessage(sendtopic, msg=msg)
        return wrapper
    return decorate


def PubSendSpecific(topic, queue=True):
    def decorate(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            msg = func(self, *args, **kwargs)
            mvcid = id(self._mvccontainer)
            sendtopic = '%d.%s' % (mvcid, topic)
            # sendtopic = topic
            if queue:
                wx.CallAfter(pub.sendMessage, sendtopic, msg=msg)
            else:
                pub.sendMessage(sendtopic, msg=msg)
        return wrapper
    return decorate
