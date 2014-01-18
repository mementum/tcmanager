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
"""Subclass of MainFrame, which is generated by wxFormBuilder."""

from collections import OrderedDict
import datetime
import itertools

import openpyxl
import xlrd
import wx

import maingui
from dialoglongop import DialogLongOp

import config
from mvcbase import ViewRole, PubSend, PubSubscribe
import rpcsupport

@ViewRole
class MainFrame(maingui.MainFrame):

    @PubSubscribe('logappend')
    def LogAppend(self, msg):
        dt = datetime.datetime.now().isoformat()
        self.m_textCtrlLog.AppendText('%s: %s\n' % (dt, msg))

    @PubSubscribe('error')
    def DisplayError(self, msg):
        wx.MessageBox(msg, 'Error')

    def DisplayWarning(self, msg):
        return wx.MessageBox(message=msg, caption='Error',
                               style= wx.ICON_HAND | wx.YES_NO)

    @PubSend('init')
    def __init__(self, parent):
        maingui.MainFrame.__init__(self, parent)

    @PubSubscribe('init')
    def OnModelInit(self, msg):
        ############################################################
        # SERVER CONFIG
        ############################################################
        self.m_textCtrlServerUrl.SetValue(self._model.serverurl)
        self.m_textCtrlServerUsername.SetValue(self._model.serverusername)
        self.m_textCtrlServerPassword.SetValue(self._model.serverpassword)
        self.m_checkBoxServerPasswordShow.SetValue(self._model.serverpasswordshow)

        ############################################################
        # UPLOAD CONFIG
        ############################################################
        self.m_filePickerExcelUpload.SetPath(self._model.uploadexcel)
        self.m_textCtrlUploadCatalogName.SetValue(self._model.uploadcatalogname)
        self.m_checkBoxUploadUseAvailableCatalog.SetValue(self._model.uploadusecatalog)
        self.m_checkBoxUploadUpdateTc.SetValue(self._model.uploadupdatetc)

        ############################################################
        # DOWNLOAD CONFIG
        ############################################################
        self.m_filePickerDownloadExcel.SetPath(self._model.downloadexcel)

        ############################################################
        # LifeCard Download CONFIG
        ############################################################
        self.m_filePickerLifeCardExcel.SetPath(self._model.lifecardexcel)
        self.m_checkBoxLifeCardOverwriteTestCases = self._model.lcovertestcases
        self.m_dirPickerDirAttachments.SetPath(self._model.lifecardattachdir)

        ############################################################
        # LifeCard Upload CONFIG
        ############################################################
        self.m_filePickerLifeCardExcelUp.SetPath(self._model.lifecardexcelup)
        self._view.m_textCtrlLifeCardAuthorUp.SetValue(self._model.lifecardauthorup)


    ############################################################
    # SERVER OPS
    ############################################################
    @PubSubscribe('catalogs')
    def OnCatalogs(self, msg):
        self.m_choiceCatalogs.Clear()
        for catalog in self._model.catalogs:
            item = self.m_choiceCatalogs.Append(catalog[2])
            self.m_choiceCatalogs.SetClientData(item, catalog)

        if self.m_choiceCatalogs.GetCount():
            self.m_choiceCatalogs.SetSelection(0)

    def DeleteCatalog(self, control, delcatalog):
        delcatid = delcatalog[0]
        for item in xrange(0, control.GetCount()):
            catalog = control.GetClientData(item)
            if catalog[0] == delcatid:
                control.Delete(item)
                break

        item -= 1
        if -1 < item < control.GetCount():
            control.SetSelection(item)


    @PubSubscribe('catalogdeleted')
    def OnCatalogDeleted(self, msg):
        self.DeleteCatalog(self.m_choiceCatalogs, msg)


    @PubSubscribe('catalogdeletedall')
    def OnCatalogDeletedAll(self, msg):
        self.m_choiceCatalogs.Clear()

    ############################################################
    # UPLOAD OPS
    ############################################################
    @PubSubscribe('uploadsheets')
    def OnUploadSheets(self, msg):
        self.m_choiceUploadSheets.AppendItems(self._model.uploadsheets)
        if self.m_choiceUploadSheets.GetCount():
            self.m_choiceUploadSheets.SetSelection(0) # Generates this an event?
            # FIXME: the view must not touch the model - Generate event for controller
            self._model.uploadsheet = self.m_choiceUploadSheets.GetStringSelection()
        else:
            self._model.uploadsheet = None

    @PubSubscribe('catalogdeleted')
    def OnUploadCatalogDeleted(self, msg):
        self.DeleteCatalog(self.m_choiceUploadCatalogs, msg)

    @PubSubscribe('catalogdeletedall')
    def OnUploadCatalogDeletedAll(self, msg):
        self.m_choiceUploadCatalogs.Clear()

    @PubSubscribe('catalogs')
    def OnUploadCatalogs(self, msg):
        self.m_choiceUploadCatalogs.Clear()
        for catalog in self._model.catalogs:
            item = self.m_choiceUploadCatalogs.Append(catalog[2])
            self.m_choiceUploadCatalogs.SetClientData(item, catalog)

        if self.m_choiceUploadCatalogs.GetCount():
            self.m_choiceUploadCatalogs.SetSelection(0)

    #@PubSubscribe('uploadingexcel')
    def UploadingExcel(self):
        self.dlgupexcel = DialogLongOp(self,
                                       message='Please do not touch anything until you see the\n'
                                       'an error in the log or the indication the\n'
                                       'the process is over',
                                       caption='Uploading Excel in progress',
                                       style=wx.ICON_EXCLAMATION | wx.OK)

        retval = self.dlgupexcel.ShowModal()
        self.dlgupexcel = None

    @PubSubscribe('uploadedexcel')
    def OnUploadedExcel(self, msg):
        if self.dlgupexcel:
            self.dlgupexcel.EndModal(wx.ID_OK)

    ############################################################
    # DOWNLOAD CONFIG
    ############################################################
    @PubSubscribe('catalogdeleted')
    def OnDownloadCatalogDeleted(self, msg):
        self.DeleteCatalog(self.m_choiceDownloadCatalogs, msg)

    @PubSubscribe('catalogdeletedall')
    def OnDownloadCatalogDeletedAll(self, msg):
        self.m_choiceDownloadCatalogs.Clear()

    @PubSubscribe('catalogs')
    def OnDownloadCatalogs(self, msg):
        self.m_choiceDownloadCatalogs.Clear()
        for catalog in self._model.catalogs:
            item = self.m_choiceDownloadCatalogs.Append(catalog[2])
            self.m_choiceDownloadCatalogs.SetClientData(item, catalog)

        if self.m_choiceDownloadCatalogs.GetCount():
            self.m_choiceDownloadCatalogs.SetSelection(0)
            # FIXME: the view must not touch the model - Generate event for controller
            self._model.downloadcatalog = catalog # catalog
        else:
            self._model.downloadcatalog = None # catalog
            
    #@PubSubscribe('downloadingexcel')
    def DownloadingExcel(self):
        self.dlgupexcel = DialogLongOp(self,
                                       message='Please do not touch anything until you see\n'
                                       'an error in the log or the indication the\n'
                                       'the process is over',
                                       caption='Downloading TestCases to Excel',
                                       style=wx.ICON_EXCLAMATION | wx.OK)

        retval = self.dlgupexcel.ShowModal()
        self.dlgupexcel = None

    @PubSubscribe('downloadedexcel')
    def OnDownloadedExcel(self, msg):
        if self.dlgupexcel:
            self.dlgupexcel.EndModal(wx.ID_OK)


    ############################################################
    # LifeCard Download
    ############################################################
    @PubSubscribe('catalogdeletedall')
    def OnLifeCardCatalogDeletedAll(self, msg):
        self.m_choiceLifeCardCatalogs.Clear()

    @PubSubscribe('catalogdeleted')
    def OnLifeCardCatalogDeleted(self, msg):
        self.DeleteCatalog(self.m_choiceLifeCardCatalogs, msg)

    @PubSubscribe('catalogs')
    def OnLifeCardCatalogs(self, msg):
        self.m_choiceLifeCardCatalogs.Clear()
        for catalog in self._model.catalogs:
            item = self.m_choiceLifeCardCatalogs.Append(catalog[2])
            self.m_choiceLifeCardCatalogs.SetClientData(item, catalog)

        if self.m_choiceLifeCardCatalogs.GetCount():
            self.m_choiceLifeCardCatalogs.SetSelection(0)
            # FIXME: the view must not touch the model - Generate event for controller
            self._model.lifecardcatalog = self.m_choiceLifeCardCatalogs.GetClientData(0)
        else:
            # FIXME: the view must not touch the model - Generate event for controller
            self._model.lifecardcatalog = None

    @PubSubscribe('testplans')
    def OnLifeCardTestPlans(self, msg):
        testplans = msg
        self.m_choiceLifeCardTestPlans.Clear()
        for testplan in testplans:
            item = self.m_choiceLifeCardTestPlans.Append(testplan[1])
            self.m_choiceLifeCardTestPlans.SetClientData(item, testplan)
        
        if self.m_choiceLifeCardTestPlans.GetCount():
            self.m_choiceLifeCardTestPlans.SetSelection(0)
            # FIXME: the view must not touch the model - Generate event for controller
            self._model.lifecardtestplan = self.m_choiceLifeCardTestPlans.GetClientData(0)
        else:
            # FIXME: the view must not touch the model - Generate event for controller
            self._model.lifecardtestplan = None

    #@PubSubscribe('lifecarddownloadingexcel')
    def LifeCardDownloadingExcel(self):
        self.dlgupexcel = DialogLongOp(self,
                                       message='Please do not touch anything until you see\n'
                                       'an error in the log or the indication the\n'
                                       'the process is over',
                                       caption='Downloading LifeCard to Excel',
                                       style=wx.ICON_EXCLAMATION | wx.OK)

        retval = self.dlgupexcel.ShowModal()
        self.dlgupexcel = None

    @PubSubscribe('lifecarddownloadedexcel')
    def OnLifeCardDownloadedExcel(self, msg):
        if self.dlgupexcel:
            self.dlgupexcel.EndModal(wx.ID_OK)


    #@PubSubscribe('lifecarddownloadingattach')
    def LifeCardDownloadingAttach(self):
        self.dlgupexcel = DialogLongOp(self,
                                       message='Please do not touch anything until you see\n'
                                       'an error in the log or the indication the\n'
                                       'the process is over',
                                       caption='Downloading LifeCard to Excel',
                                       style=wx.ICON_EXCLAMATION | wx.OK)

        retval = self.dlgupexcel.ShowModal()
        self.dlgupexcel = None

    @PubSubscribe('lifecarddownloadedattach')
    def OnLifeCardDownloadedAttach(self, msg):
        if self.dlgupexcel:
            self.dlgupexcel.EndModal(wx.ID_OK)

    ############################################################
    # LifeCard Download
    ############################################################

    #@PubSubscribe('lifecarduploading')
    def LifeCardUploading(self):
        self.dlgupexcel = DialogLongOp(self,
                                       message='Please do not touch anything until you see\n'
                                       'an error in the log or the indication the\n'
                                       'the process is over',
                                       caption='Downloading LifeCard to Excel',
                                       style=wx.ICON_EXCLAMATION | wx.OK)

        retval = self.dlgupexcel.ShowModal()
        self.dlgupexcel = None

    @PubSubscribe('lifecarduploaded')
    def OnLifeCardUploaded(self, msg):
        if self.dlgupexcel:
            self.dlgupexcel.EndModal(wx.ID_OK)
