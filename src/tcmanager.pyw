#!/usr/bin/env python
# -*- coding: utf-8; py-indent-offset:4 -*-
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
import wx

import flushfile
from mvcbase import MvcContainer

from controller import Controller
from mainframe import MainFrame
from model import Model
import constants

appname=constants.Appname
vendorname=constants.Vendorname

@MvcContainer
class MainApp(wx.App):
    def OnInit(self):
        self.name = '%s-%s' % (appname, wx.GetUserId())
        self.instance = wx.SingleInstanceChecker(self.name)
        if self.instance.IsAnotherRunning():
            wx.MessageBox("Another instance is running", "ERROR")
            return False

        wx.Log_SetActiveTarget(wx.LogStderr())
        # wx.Log_SetActiveTarget(wx.LogBuffer())

        self.SetAppName(appname)
        self.SetVendorName(vendorname)
        config = wx.Config()
        config.SetRecordDefaults(True)

        self._model = Model()
        self._controller = Controller()
        self._view = view = MainFrame(parent=None)
        self.SetTopWindow(view)
        view.Show(True)

        return True

if __name__ == '__main__':
    app = MainApp(redirect=False) # avoid creation of popup
    app.MainLoop()
