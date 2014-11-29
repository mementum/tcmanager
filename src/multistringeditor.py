#!/usr/bin/env python
# -*- coding: latin-1; py-indent-offset:4 -*-
################################################################################
# 
#  Copyright (C) 2014 Daniel Rodriguez
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
################################################################################

import wx
import wx.lib

import maingui


class MultiStringEditor(maingui.MultiStringEditor):

    def __init__(self, parent, title=None, items=None):
        maingui.MultiStringEditor.__init__(self, parent)

        self.SetTitle(title) if title else None
        self.SetItems(items) if items else None

    def SetItems(self, items, reverse=False):
        self.m_listBoxItems.SetItems(items)

    def GetItems(self):
        return self.m_listBoxItems.GetItems()

    def OnButtonClickSortAsc(self, event):
        self.SetItems(sorted(self.GetItems()))
        
    def OnButtonClickSortDesc(self, event):
        self.SetItems(sorted(self.GetItems(), reverse=True))

    def OnButtonClickAdd(self, event):
        dlg = wx.lib.textEntryDialog(parent=self, message='', title='Add Server Url')
        retcode = dlg.ShowModal()

        if retcode == wx.OK:
            self.AppendItem(dlg.GetValue())
