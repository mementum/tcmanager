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

from mvcbase import ControllerRole, PubSubscribe, ViewManager

@ControllerRole
class Controller(object):

    def __init__(self):
        pass

    @ViewManager
    def OnButtonClickResetSize(self, event):
        event.Skip()
        self._view.Fit()

    @ViewManager
    def OnSizeMainFrame(self, event):
        event.Skip()
        if not self._view.skipsize:
            wsize = event.GetSize()
            self._model.winwidth = wsize.width
            self._model.winheight = wsize.height

    @PubSubscribe('init')
    def OnViewInit(self, msg):
        self._model.init()

    @ViewManager
    def OnButtonClickClearRegistry(self, event):
        wx.Config.Get().DeleteAll()

    @ViewManager
    def OnButtonClickExit(self, event):
        self._view.Destroy()

    @ViewManager
    def OnButtonClearLog(self, event):
        self._view.m_textCtrlLog.Clear()
        

    ############################################################
    # SERVER CONFIG
    ############################################################
    @ViewManager
    def OnKillFocusServerUrl(self, event):
        self._model.serverurl = self._view.m_textCtrlServerUrl.GetValue()

    @ViewManager
    def OnKillFocusServerUsername(self, event):
        self._model.serverusername = self._view.m_textCtrlServerUsername.GetValue()

    @ViewManager
    def OnKillFocusServerPassword(self, event):
        self._model.serverpassword = self._view.m_textCtrlServerPassword.GetValue()

    @ViewManager
    def OnCheckBoxShowServerPassword(self, event):
        self._model.serverpasswordshow = ischecked = event.IsChecked()
        if ischecked:
            ctrlshow = self._view.m_textCtrlServerPasswordShown
            ctrlhide = self._view.m_textCtrlServerPassword
        else:
            ctrlhide = self._view.m_textCtrlServerPasswordShown
            ctrlshow = self._view.m_textCtrlServerPassword

        curpass = ctrlhide.GetValue()
        ctrlshow.SetValue(curpass)
        ctrlhide.Hide()
        ctrlshow.Show()
        ctrlshow.GetParent().GetSizer().Layout() # to ensure corrent presentation
        self._view.Refresh() # seems not needed but ...

    @ViewManager
    def OnButtonClickApplyServerSettings(self, event):
        pass

    @ViewManager
    def OnButtonClickCatalogsDelete(self, event):
        item = self._view.m_choiceCatalogs.GetSelection()
        if item == wx.NOT_FOUND:
            return
        catalog = self._view.m_choiceCatalogs.GetClientData(item)
        self._model.DeleteCatalog(catalog)

    @ViewManager
    def OnButtonClickCatalogsDeleteAll(self, event):
        self._model.DeleteCatalogAll()
        

    ############################################################
    # UPLOAD TESTCASES
    ############################################################
    @ViewManager
    def OnFileChangedExcelUpload(self, event):
        self._model.uploadexcel = self._view.m_filePickerExcelUpload.GetPath()
        self._view.m_choiceUploadSheets.Clear() # Clear Sheets from previous File
        if self._model.uploadautosheets:
            self._model.GetUploadSheets()

    @ViewManager
    def OnChoiceUploadSheets(self, event):
        self._model.uploadsheet = self._view.m_choiceUploadSheets.GetStringSelection()

    @ViewManager
    def OnButtonClickUploadReloadSheets(self, event):
        self._view.m_choiceUploadSheets.Clear() # Clear Sheets before refreshing
        self._model.GetUploadSheets()

    @ViewManager
    def OnButtonClickUploadReloadCatalogs(self, event):
        self._view.m_choiceCatalogs.Clear() # Clear Catalogs
        self._view.m_choiceDownloadCatalogs.Clear() # Clear Catalogs
        self._view.m_choiceUploadCatalogs.Clear() # Clear Catalogs
        self._view.m_choiceLifeCardCatalogs.Clear() # Clear Catalogs
        self._model.GetUploadCatalogs()

    @ViewManager
    def OnCheckBoxUploadUseAvailableCatalog(self, event):
        self._model.uploadusecatalog = event.IsChecked()

    @ViewManager
    def OnCheckBoxUploadUpdateTc(self, event):
        self._model.uploadupdatetc = event.IsChecked()

    @ViewManager
    def OnKillFocusUploadCatalogName(self, event):
        self._model.uploadcatalogname = self._view.m_textCtrlUploadCatalogName.GetValue()

    @ViewManager
    def OnButtonClickUploadExcel(self, event):
        catname = self._model.uploadcatalogname
        # First check if there is any catalog name
        if not self._model.uploadusecatalog and not catname:
            self._view.DisplayError('No Catalog Name given')
            return

        if not self._model.uploadusecatalog and catname in self._model.catalogs:
            self._view.DisplayError('Existing Catalog. Delete it first')
            return

        if self._model.uploadusecatalog:
            item = self._view.m_choiceUploadCatalogs.GetSelection()
            catalog = self._view.m_choiceUploadCatalogs.GetClientData(item)
            self._model.uploadusecatalogname = self._view.m_choiceUploadCatalogs.GetStringSelection()
            self._model.uploadusecatalogid = catalog[0]

        self._model.UploadExcel()
        self._view.UploadingExcel()


    ############################################################
    # DOWNLOAD TESTCASES
    ############################################################
    @ViewManager
    def OnChoiceDownloadCatalogs(self, event):
        item = self._view.m_choiceDownloadCatalogs.GetSelection()
        catalog = self._view.m_choiceDownloadCatalogs.GetClientData(item)
        self._model.downloadcatalog = catalog # catalog
        
    @ViewManager
    def OnFileChangedDownloadExcel(self, event):
        filename = self._view.m_filePickerDownloadExcel.GetPath()
        self._model.downloadexcel = filename


    @ViewManager
    def OnButtonClickDownloadExcel(self, event):
        self._model.DownloadExcel()
        self._view.DownloadingExcel()

    ############################################################
    # LifeCard Download
    ############################################################
    @ViewManager
    def OnCheckBoxDownloadOpen(self, event):
        self._model.lcdownopen = event.IsChecked()

    @ViewManager
    def OnCheckBoxDownloadFixed(self, event):
        self._model.lcdownfixed = event.IsChecked()

    @ViewManager
    def OnCheckBoxDownloadClosed(self, event):
        self._model.lcdownclosed = event.IsChecked()

    @ViewManager
    def OnCheckBoxDownloadInvestigation(self, event):
        self._model.lcdowninvest = event.IsChecked()

    @ViewManager
    def OnCheckBoxDownloadRejected(self, event):
        self._model.lcdownreject = event.IsChecked()

    @ViewManager
    def OnCheckBoxDownloadNew(self, event):
        self._model.lcdownnew = event.IsChecked()


    @ViewManager
    def OnChoiceLifeCardCatalogs(self, event):
        item = self._view.m_choiceLifeCardCatalogs.GetSelection()
        catalog = self._view.m_choiceDownloadCatalogs.GetClientData(item)
        self._model.lifecardcatalog = catalog
        self._model.GetTestPlans(catalog)

    @ViewManager
    def OnChoiceLifeCardTestPlans(self, event):
        item = self._view.m_choiceLifeCardTestPlans.GetSelection()
        testplan = self._view.m_choiceDownloadTestPlans.GetClientData(item)
        self._model.lifecardtestplan = testplan

    @ViewManager
    def OnButtonClickLifeCardTestPlansReload(self, event):
        item = self._view.m_choiceLifeCardCatalogs.GetSelection()
        if item == wx.NOT_FOUND:
            return
        catalog = self._view.m_choiceDownloadCatalogs.GetClientData(item)
        self._model.GetTestPlans(catalog)

    @ViewManager
    def OnFileChangedLifeCardExcel(self, event):
        self._model.lifecardexcel = self._view.m_filePickerLifeCardExcel.GetPath()

    @ViewManager
    def OnButtonClickLifeCardDownload(self, event):
        self._model.LifeCardDownloadExcel()
        self._view.LifeCardDownloadingExcel()

    @ViewManager
    def OnCheckBoxDownloadKeepExcelOpen(self, event):
        self._model.lcdownkeepexcelopen = event.IsChecked()

    @ViewManager
    def OnCheckBoxDownloadExcelNotSave(self, event):
        self._model.lcdownexcelnotsave = event.IsChecked()

    @ViewManager
    def OnCheckBoxLcDownMakeCopy(self, event):
        self._model.lcdownmakecopy = event.IsChecked()

    @ViewManager
    def OnCheckBoxLcDownFilterVendorComments(self, event):
        self._model.lcdownfiltervendorcomments = event.IsChecked()

    @ViewManager
    def OnCheckBoxLcDownCopyWithVendorComments(self, event):
        self._model.lcdowncopywithvendorcomments = event.IsChecked()

    @ViewManager
    def OnDirChangedDirAttachments(self, event):
        self._model.lifecardattachdir = self._view.m_dirPickerDirAttachments.GetPath()

    ############################################################
    # LifeCard Attachment Download
    ############################################################
    @ViewManager
    def OnButtonClickDownloadAttachments(self, event):
        self._model.LifeCardDownloadAttach()
        self._view.LifeCardDownloadingAttach()

    @ViewManager
    def OnCheckBoxLcDownAttachOpen(self, event):
        self._model.lcdownattachopen = event.IsChecked()

    @ViewManager
    def OnCheckBoxLcDownAttachClosed(self, event):
        self._model.lcdownattachclosed = event.IsChecked()

    @ViewManager
    def OnCheckBoxLcDownAttachInvestigation(self, event):
        self._model.lcdownattachinvestigation = event.IsChecked()

    @ViewManager
    def OnCheckBoxLcDownAttachFixed(self, event):
        self._model.lcdownattachfixed = event.IsChecked()

    @ViewManager
    def OnCheckBoxLcDownAttachRejected(self, event):
        self._model.lcdownattachrejected = event.IsChecked()

    @ViewManager
    def OnCheckBoxLcDownAttachNew(self, event):
        self._model.lcdownattachnew = event.IsChecked()

    ############################################################
    # LifeCard Upload
    ############################################################
    @ViewManager
    def OnCheckBoxLifeCardUpStatusOpen(self, event):
        self._model.lcardup_status_open = event.IsChecked()

    @ViewManager
    def OnCheckBoxLifeCardUpStatusClosed(self, event):
        self._model.lcardup_status_closed = event.IsChecked()

    @ViewManager
    def OnCheckBoxLifeCardUpStatusInvestigation(self, event):
        self._model.lcardup_status_investigation = event.IsChecked()

    @ViewManager
    def OnCheckBoxLifeCardUpStatusFixed(self, event):
        self._model.lcardup_status_fixed = event.IsChecked()

    @ViewManager
    def OnCheckBoxLifeCardUpStatusRejected(self, event):
        self._model.lcardup_status_rejected = event.IsChecked()

    @ViewManager
    def OnCheckBoxLifeCardUpStatusNew(self, event):
        self._model.lcardup_status_new = event.IsChecked()

    @ViewManager
    def OnKillFocusLifeCardUpSheetName(self, event):
        self._model.lcardup_sheetname = self._view.m_textCtrlLifeCardUpSheetName.GetValue()
    
    @ViewManager
    def OnKillFocusLifeCardUpColRowStart(self, event):
        self._model.lcardup_row_start = self._view.m_textCtrlLifeCardUpRowStart.GetValue()

    @ViewManager
    def OnKillFocusLifeCardUpColTicketId(self, event):
        self._model.lcardup_col_ticket = self._view.m_textCtrlLifeCardUpColTicketId.GetValue()

    @ViewManager
    def OnKillFocusLifeCardUpColResolution(self, event):
        self._model.lcardup_col_resol = self._view.m_textCtrlLifeCardUpColResolution.GetValue()

    @ViewManager
    def OnKillFocusLifeCardUpColComment(self, event):
        self._model.lcardup_col_comment = self._view.m_textCtrlLifeCardUpColComment.GetValue()

    @ViewManager
    def OnFileChangedLifeCardExcelUp(self, event):
        self._model.lifecardexcelup = self._view.m_filePickerLifeCardExcelUp.GetPath()

    @ViewManager
    def OnKillFocuslLifeCardAuthorUp(self, event):
        self._model.lifecardauthorup = self._view.m_textCtrlLifeCardAuthorUp.GetValue()

    @ViewManager
    def OnButtonClickLifeCardUpload(self, event):
        self._model.LifeCardUpload()
        self._view.LifeCardUploading()
