# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Oct  8 2012)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Test Case Manager", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel6 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer16 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_notebook1 = wx.Notebook( self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.NB_BOTTOM )
		self.m_panel8 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer12 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer13 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel8, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )
		
		bSizer13 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText7 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"Server Url", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		bSizer13.Add( self.m_staticText7, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrlServerUrl = wx.TextCtrl( self.m_panel8, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		bSizer13.Add( self.m_textCtrlServerUrl, 1, wx.ALL, 5 )
		
		
		sbSizer13.Add( bSizer13, 0, wx.EXPAND, 5 )
		
		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText3 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		bSizer8.Add( self.m_staticText3, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_textCtrlServerUsername = wx.TextCtrl( self.m_panel8, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.m_textCtrlServerUsername, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText4 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		bSizer8.Add( self.m_staticText4, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
		
		self.m_panel5 = wx.Panel( self.m_panel8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer181 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_textCtrlServerPassword = wx.TextCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		bSizer181.Add( self.m_textCtrlServerPassword, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		self.m_textCtrlServerPasswordShown = wx.TextCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrlServerPasswordShown.Hide()
		
		bSizer181.Add( self.m_textCtrlServerPasswordShown, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel5.SetSizer( bSizer181 )
		self.m_panel5.Layout()
		bSizer181.Fit( self.m_panel5 )
		bSizer8.Add( self.m_panel5, 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		sbSizer13.Add( bSizer8, 0, wx.EXPAND, 5 )
		
		self.m_checkBoxServerPasswordShow = wx.CheckBox( self.m_panel8, wx.ID_ANY, u"Show Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer13.Add( self.m_checkBoxServerPasswordShow, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline7 = wx.StaticLine( self.m_panel8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		sbSizer13.Add( self.m_staticline7, 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5 )
		
		self.m_button10 = wx.Button( self.m_panel8, wx.ID_ANY, u"Test Server Connection", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button10.Enable( False )
		
		sbSizer13.Add( self.m_button10, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer12.Add( sbSizer13, 1, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel8, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )
		
		self.m_checkBox6 = wx.CheckBox( self.m_panel8, wx.ID_ANY, u"Check Server Connection on Start", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox6.Enable( False )
		
		sbSizer5.Add( self.m_checkBox6, 0, wx.ALL, 5 )
		
		
		bSizer12.Add( sbSizer5, 0, wx.EXPAND, 5 )
		
		sbSizer6 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel8, wx.ID_ANY, u"Test Catalogs" ), wx.VERTICAL )
		
		bSizer22 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText151 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"Available Catalogs", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText151.Wrap( -1 )
		bSizer22.Add( self.m_staticText151, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_choiceCatalogsChoices = []
		self.m_choiceCatalogs = wx.Choice( self.m_panel8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choiceCatalogsChoices, 0 )
		self.m_choiceCatalogs.SetSelection( 0 )
		bSizer22.Add( self.m_choiceCatalogs, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_button16 = wx.Button( self.m_panel8, wx.ID_ANY, u"Refresh", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer22.Add( self.m_button16, 0, wx.ALL, 5 )
		
		
		sbSizer6.Add( bSizer22, 1, wx.EXPAND, 5 )
		
		bSizer23 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button14 = wx.Button( self.m_panel8, wx.ID_ANY, u"Delete Selected", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer23.Add( self.m_button14, 0, wx.ALL, 5 )
		
		self.m_button15 = wx.Button( self.m_panel8, wx.ID_ANY, u"Delete All", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer23.Add( self.m_button15, 0, wx.ALL, 5 )
		
		
		sbSizer6.Add( bSizer23, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer12.Add( sbSizer6, 0, wx.EXPAND, 5 )
		
		
		self.m_panel8.SetSizer( bSizer12 )
		self.m_panel8.Layout()
		bSizer12.Fit( self.m_panel8 )
		self.m_notebook1.AddPage( self.m_panel8, u"Configuration", False )
		self.m_panel9 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel9, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )
		
		fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer2.AddGrowableCol( 1 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText13 = wx.StaticText( self.m_panel9, wx.ID_ANY, u"Excel File", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )
		fgSizer2.Add( self.m_staticText13, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_filePickerExcelUpload = wx.FilePickerCtrl( self.m_panel9, wx.ID_ANY, wx.EmptyString, u"Select a file", u"Excel Files (*.xlsx;*.xls)|*.xlsx;*.xls|All Files (*.*)|*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_CHANGE_DIR|wx.FLP_DEFAULT_STYLE )
		fgSizer2.Add( self.m_filePickerExcelUpload, 0, wx.EXPAND|wx.ALL, 5 )
		
		
		fgSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		bSizer191 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_checkBoxUploadSheetsAutoRefresh = wx.CheckBox( self.m_panel9, wx.ID_ANY, u"Auto Refresh Sheets on Start and New File Chosen", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBoxUploadSheetsAutoRefresh.Enable( False )
		
		bSizer191.Add( self.m_checkBoxUploadSheetsAutoRefresh, 0, wx.ALL, 5 )
		
		
		fgSizer2.Add( bSizer191, 1, wx.EXPAND, 5 )
		
		self.m_staticText8 = wx.StaticText( self.m_panel9, wx.ID_ANY, u"Available Sheets", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		fgSizer2.Add( self.m_staticText8, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		m_choiceUploadSheetsChoices = []
		self.m_choiceUploadSheets = wx.Choice( self.m_panel9, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choiceUploadSheetsChoices, 0 )
		self.m_choiceUploadSheets.SetSelection( 0 )
		bSizer3.Add( self.m_choiceUploadSheets, 1, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
		
		self.m_button1 = wx.Button( self.m_panel9, wx.ID_ANY, u"Refresh", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		fgSizer2.Add( bSizer3, 0, wx.EXPAND|wx.BOTTOM|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticline15 = wx.StaticLine( self.m_panel9, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer2.Add( self.m_staticline15, 0, wx.EXPAND|wx.TOP|wx.BOTTOM|wx.LEFT|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		self.m_staticline16 = wx.StaticLine( self.m_panel9, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer2.Add( self.m_staticline16, 0, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		self.m_staticText10 = wx.StaticText( self.m_panel9, wx.ID_ANY, u"Available Catalogs", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )
		fgSizer2.Add( self.m_staticText10, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer18 = wx.BoxSizer( wx.HORIZONTAL )
		
		m_choiceUploadCatalogsChoices = []
		self.m_choiceUploadCatalogs = wx.Choice( self.m_panel9, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choiceUploadCatalogsChoices, 0 )
		self.m_choiceUploadCatalogs.SetSelection( 0 )
		bSizer18.Add( self.m_choiceUploadCatalogs, 1, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
		
		self.m_buttonUploadReloadCatalogs = wx.Button( self.m_panel9, wx.ID_ANY, u"Refresh", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer18.Add( self.m_buttonUploadReloadCatalogs, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		fgSizer2.Add( bSizer18, 0, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		fgSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		bSizer20 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_checkBoxUploadAutoLoadCatalogs = wx.CheckBox( self.m_panel9, wx.ID_ANY, u"Auto load catalogs on Start or Server Change", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBoxUploadAutoLoadCatalogs.Enable( False )
		
		bSizer20.Add( self.m_checkBoxUploadAutoLoadCatalogs, 0, wx.ALL, 5 )
		
		
		fgSizer2.Add( bSizer20, 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText1 = wx.StaticText( self.m_panel9, wx.ID_ANY, u"New Catalog", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		fgSizer2.Add( self.m_staticText1, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		bSizer30 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_textCtrlUploadCatalogName = wx.TextCtrl( self.m_panel9, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer30.Add( self.m_textCtrlUploadCatalogName, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )
		
		
		fgSizer2.Add( bSizer30, 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		sbSizer3.Add( fgSizer2, 1, wx.EXPAND, 5 )
		
		bSizer19 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_checkBoxUploadUseAvailableCatalog = wx.CheckBox( self.m_panel9, wx.ID_ANY, u"Use Available Catalog", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer19.Add( self.m_checkBoxUploadUseAvailableCatalog, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline9 = wx.StaticLine( self.m_panel9, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer19.Add( self.m_staticline9, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_checkBoxUploadUpdateTc = wx.CheckBox( self.m_panel9, wx.ID_ANY, u"Update Test Cases", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer19.Add( self.m_checkBoxUploadUpdateTc, 0, wx.ALL, 5 )
		
		
		sbSizer3.Add( bSizer19, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer2.Add( sbSizer3, 0, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		self.m_button2 = wx.Button( self.m_panel9, wx.ID_ANY, u"Upload to Server", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_button2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.m_panel9.SetSizer( bSizer2 )
		self.m_panel9.Layout()
		bSizer2.Fit( self.m_panel9 )
		self.m_notebook1.AddPage( self.m_panel9, u"Test Cases Upload", False )
		self.m_panel10 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer11 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer32 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel10, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )
		
		fgSizer21 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer21.AddGrowableCol( 1 )
		fgSizer21.SetFlexibleDirection( wx.BOTH )
		fgSizer21.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText15 = wx.StaticText( self.m_panel10, wx.ID_ANY, u"Test Catalogs", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )
		fgSizer21.Add( self.m_staticText15, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer29 = wx.BoxSizer( wx.HORIZONTAL )
		
		m_choiceDownloadCatalogsChoices = []
		self.m_choiceDownloadCatalogs = wx.Choice( self.m_panel10, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choiceDownloadCatalogsChoices, 0 )
		self.m_choiceDownloadCatalogs.SetSelection( 0 )
		bSizer29.Add( self.m_choiceDownloadCatalogs, 1, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
		
		self.m_button11 = wx.Button( self.m_panel10, wx.ID_ANY, u"Refresh", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer29.Add( self.m_button11, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		fgSizer21.Add( bSizer29, 1, wx.EXPAND, 5 )
		
		self.m_staticline13 = wx.StaticLine( self.m_panel10, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer21.Add( self.m_staticline13, 1, wx.TOP|wx.BOTTOM|wx.LEFT|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		self.m_staticline14 = wx.StaticLine( self.m_panel10, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer21.Add( self.m_staticline14, 1, wx.EXPAND|wx.TOP|wx.BOTTOM|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText91 = wx.StaticText( self.m_panel10, wx.ID_ANY, u"Excel File", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText91.Wrap( -1 )
		fgSizer21.Add( self.m_staticText91, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer171 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_filePickerDownloadExcel = wx.FilePickerCtrl( self.m_panel10, wx.ID_ANY, wx.EmptyString, u"Select a file", u"Excel Files (*.xlsx;*.xls)|*.xlsx;*.xls|All Files (*.*)|*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_CHANGE_DIR|wx.FLP_OVERWRITE_PROMPT|wx.FLP_SAVE|wx.FLP_USE_TEXTCTRL )
		bSizer171.Add( self.m_filePickerDownloadExcel, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		fgSizer21.Add( bSizer171, 1, wx.EXPAND, 5 )
		
		
		sbSizer32.Add( fgSizer21, 1, wx.EXPAND, 5 )
		
		
		bSizer11.Add( sbSizer32, 0, wx.EXPAND, 5 )
		
		
		bSizer11.AddSpacer( ( 0, 0), 0, wx.EXPAND, 5 )
		
		self.m_button21 = wx.Button( self.m_panel10, wx.ID_ANY, u"Download from Server", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.m_button21, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.m_panel10.SetSizer( bSizer11 )
		self.m_panel10.Layout()
		bSizer11.Fit( self.m_panel10 )
		self.m_notebook1.AddPage( self.m_panel10, u"Test Cases Download", False )
		self.m_panel7 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer24 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer321 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel7, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )
		
		fgSizer211 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer211.AddGrowableCol( 1 )
		fgSizer211.SetFlexibleDirection( wx.BOTH )
		fgSizer211.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText152 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Test Catalogs", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText152.Wrap( -1 )
		fgSizer211.Add( self.m_staticText152, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer291 = wx.BoxSizer( wx.HORIZONTAL )
		
		m_choiceLifeCardCatalogsChoices = []
		self.m_choiceLifeCardCatalogs = wx.Choice( self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choiceLifeCardCatalogsChoices, 0 )
		self.m_choiceLifeCardCatalogs.SetSelection( 0 )
		bSizer291.Add( self.m_choiceLifeCardCatalogs, 1, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
		
		self.m_button111 = wx.Button( self.m_panel7, wx.ID_ANY, u"Refresh", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer291.Add( self.m_button111, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		fgSizer211.Add( bSizer291, 1, wx.EXPAND, 5 )
		
		self.m_staticText20 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Test Plans", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )
		fgSizer211.Add( self.m_staticText20, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer292 = wx.BoxSizer( wx.HORIZONTAL )
		
		m_choiceLifeCardTestPlansChoices = []
		self.m_choiceLifeCardTestPlans = wx.Choice( self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choiceLifeCardTestPlansChoices, 0 )
		self.m_choiceLifeCardTestPlans.SetSelection( 0 )
		bSizer292.Add( self.m_choiceLifeCardTestPlans, 1, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
		
		self.m_button19 = wx.Button( self.m_panel7, wx.ID_ANY, u"Refresh", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer292.Add( self.m_button19, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		fgSizer211.Add( bSizer292, 1, wx.EXPAND, 5 )
		
		self.m_staticline131 = wx.StaticLine( self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer211.Add( self.m_staticline131, 1, wx.TOP|wx.BOTTOM|wx.LEFT|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		self.m_staticline141 = wx.StaticLine( self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer211.Add( self.m_staticline141, 1, wx.EXPAND|wx.TOP|wx.BOTTOM|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText911 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"LifeCard", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText911.Wrap( -1 )
		fgSizer211.Add( self.m_staticText911, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer1711 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_filePickerLifeCardExcel = wx.FilePickerCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, u"Select a file", u"Excel Files (*.xlsx;*.xls)|*.xlsx;*.xls|All Files (*.*)|*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_CHANGE_DIR|wx.FLP_OVERWRITE_PROMPT|wx.FLP_SAVE|wx.FLP_USE_TEXTCTRL )
		bSizer1711.Add( self.m_filePickerLifeCardExcel, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		fgSizer211.Add( bSizer1711, 1, wx.EXPAND, 5 )
		
		
		fgSizer211.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_checkBoxLifeCardOverwriteTestCases = wx.CheckBox( self.m_panel7, wx.ID_ANY, u"Overwrite Test Cases in Excel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBoxLifeCardOverwriteTestCases.Enable( False )
		
		fgSizer211.Add( self.m_checkBoxLifeCardOverwriteTestCases, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		sbSizer321.Add( fgSizer211, 1, wx.EXPAND, 5 )
		
		
		bSizer24.Add( sbSizer321, 0, wx.EXPAND, 5 )
		
		self.m_staticline142 = wx.StaticLine( self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer24.Add( self.m_staticline142, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer26 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button20 = wx.Button( self.m_panel7, wx.ID_ANY, u"Download TestCases to LifeCard", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer26.Add( self.m_button20, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_button17 = wx.Button( self.m_panel7, wx.ID_ANY, u"Download Bugs to LifeCard", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer26.Add( self.m_button17, 0, wx.ALL, 5 )
		
		
		bSizer24.Add( bSizer26, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.m_panel7.SetSizer( bSizer24 )
		self.m_panel7.Layout()
		bSizer24.Fit( self.m_panel7 )
		self.m_notebook1.AddPage( self.m_panel7, u"LifeCard Download", True )
		
		bSizer16.Add( self.m_notebook1, 1, wx.EXPAND, 5 )
		
		self.m_staticline8 = wx.StaticLine( self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer16.Add( self.m_staticline8, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer10 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText5 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Operations Log", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		bSizer10.Add( self.m_staticText5, 0, wx.ALL, 5 )
		
		self.m_textCtrlLog = wx.TextCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 600,200 ), wx.TE_MULTILINE|wx.TE_READONLY )
		bSizer10.Add( self.m_textCtrlLog, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button7 = wx.Button( self.m_panel6, wx.ID_ANY, u"Clear Log", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_button7, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_button6 = wx.Button( self.m_panel6, wx.ID_ANY, u"Exit", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_button6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_button5 = wx.Button( self.m_panel6, wx.ID_ANY, u"Clear Registry", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_button5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer10.Add( bSizer9, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP|wx.BOTTOM, 5 )
		
		
		bSizer16.Add( bSizer10, 0, wx.EXPAND, 5 )
		
		
		self.m_panel6.SetSizer( bSizer16 )
		self.m_panel6.Layout()
		bSizer16.Fit( self.m_panel6 )
		bSizer1.Add( self.m_panel6, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		bSizer1.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_textCtrlServerUrl.Bind( wx.EVT_KILL_FOCUS, self.OnKillFocusServerUrl )
		self.m_textCtrlServerUsername.Bind( wx.EVT_KILL_FOCUS, self.OnKillFocusServerUsername )
		self.m_textCtrlServerPassword.Bind( wx.EVT_KILL_FOCUS, self.OnKillFocusServerPassword )
		self.m_textCtrlServerPasswordShown.Bind( wx.EVT_KILL_FOCUS, self.OnKillFocusServerPassword )
		self.m_checkBoxServerPasswordShow.Bind( wx.EVT_CHECKBOX, self.OnCheckBoxShowServerPassword )
		self.m_button10.Bind( wx.EVT_BUTTON, self.OnButtonClickApplyServerSettings )
		self.m_button16.Bind( wx.EVT_BUTTON, self.OnButtonClickUploadReloadCatalogs )
		self.m_button14.Bind( wx.EVT_BUTTON, self.OnButtonClickCatalogsDelete )
		self.m_button15.Bind( wx.EVT_BUTTON, self.OnButtonClickCatalogsDeleteAll )
		self.m_filePickerExcelUpload.Bind( wx.EVT_FILEPICKER_CHANGED, self.OnFileChangedExcelUpload )
		self.m_checkBoxUploadSheetsAutoRefresh.Bind( wx.EVT_CHECKBOX, self.OnCheckBoxUploadAutoLoadSheets )
		self.m_choiceUploadSheets.Bind( wx.EVT_CHOICE, self.OnChoiceUploadSheets )
		self.m_button1.Bind( wx.EVT_BUTTON, self.OnButtonClickUploadReloadSheets )
		self.m_buttonUploadReloadCatalogs.Bind( wx.EVT_BUTTON, self.OnButtonClickUploadReloadCatalogs )
		self.m_checkBoxUploadAutoLoadCatalogs.Bind( wx.EVT_CHECKBOX, self.OnCheckBoxUploadAutoLoadCatalogs )
		self.m_textCtrlUploadCatalogName.Bind( wx.EVT_KILL_FOCUS, self.OnKillFocusUploadCatalogName )
		self.m_checkBoxUploadUseAvailableCatalog.Bind( wx.EVT_CHECKBOX, self.OnCheckBoxUploadUseAvailableCatalog )
		self.m_checkBoxUploadUpdateTc.Bind( wx.EVT_CHECKBOX, self.OnCheckBoxUploadUpdateTc )
		self.m_button2.Bind( wx.EVT_BUTTON, self.OnButtonClickUploadExcel )
		self.m_choiceDownloadCatalogs.Bind( wx.EVT_CHOICE, self.OnChoiceDownloadCatalogs )
		self.m_button11.Bind( wx.EVT_BUTTON, self.OnButtonClickUploadReloadCatalogs )
		self.m_filePickerDownloadExcel.Bind( wx.EVT_FILEPICKER_CHANGED, self.OnFileChangedDownloadExcel )
		self.m_button21.Bind( wx.EVT_BUTTON, self.OnButtonClickDownloadExcel )
		self.m_choiceLifeCardCatalogs.Bind( wx.EVT_CHOICE, self.OnChoiceLifeCardCatalogs )
		self.m_button111.Bind( wx.EVT_BUTTON, self.OnButtonClickUploadReloadCatalogs )
		self.m_button19.Bind( wx.EVT_BUTTON, self.OnButtonClickLifeCardTestPlansReload )
		self.m_filePickerLifeCardExcel.Bind( wx.EVT_FILEPICKER_CHANGED, self.OnFileChangedLifeCardExcel )
		self.m_checkBoxLifeCardOverwriteTestCases.Bind( wx.EVT_CHECKBOX, self.OnCheckBoxLifeCardOverwriteTestCases )
		self.m_button20.Bind( wx.EVT_BUTTON, self.OnButtonClickLifeCardDownload )
		self.m_button17.Bind( wx.EVT_BUTTON, self.OnButtonClickLifeCardDownloadBugs )
		self.m_button7.Bind( wx.EVT_BUTTON, self.OnButtonClearLog )
		self.m_button6.Bind( wx.EVT_BUTTON, self.OnButtonClickExit )
		self.m_button5.Bind( wx.EVT_BUTTON, self.OnButtonClickClearRegistry )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnKillFocusServerUrl( self, event ):
		event.Skip()
	
	def OnKillFocusServerUsername( self, event ):
		event.Skip()
	
	def OnKillFocusServerPassword( self, event ):
		event.Skip()
	
	
	def OnCheckBoxShowServerPassword( self, event ):
		event.Skip()
	
	def OnButtonClickApplyServerSettings( self, event ):
		event.Skip()
	
	def OnButtonClickUploadReloadCatalogs( self, event ):
		event.Skip()
	
	def OnButtonClickCatalogsDelete( self, event ):
		event.Skip()
	
	def OnButtonClickCatalogsDeleteAll( self, event ):
		event.Skip()
	
	def OnFileChangedExcelUpload( self, event ):
		event.Skip()
	
	def OnCheckBoxUploadAutoLoadSheets( self, event ):
		event.Skip()
	
	def OnChoiceUploadSheets( self, event ):
		event.Skip()
	
	def OnButtonClickUploadReloadSheets( self, event ):
		event.Skip()
	
	
	def OnCheckBoxUploadAutoLoadCatalogs( self, event ):
		event.Skip()
	
	def OnKillFocusUploadCatalogName( self, event ):
		event.Skip()
	
	def OnCheckBoxUploadUseAvailableCatalog( self, event ):
		event.Skip()
	
	def OnCheckBoxUploadUpdateTc( self, event ):
		event.Skip()
	
	def OnButtonClickUploadExcel( self, event ):
		event.Skip()
	
	def OnChoiceDownloadCatalogs( self, event ):
		event.Skip()
	
	
	def OnFileChangedDownloadExcel( self, event ):
		event.Skip()
	
	def OnButtonClickDownloadExcel( self, event ):
		event.Skip()
	
	def OnChoiceLifeCardCatalogs( self, event ):
		event.Skip()
	
	
	def OnButtonClickLifeCardTestPlansReload( self, event ):
		event.Skip()
	
	def OnFileChangedLifeCardExcel( self, event ):
		event.Skip()
	
	def OnCheckBoxLifeCardOverwriteTestCases( self, event ):
		event.Skip()
	
	def OnButtonClickLifeCardDownload( self, event ):
		event.Skip()
	
	def OnButtonClickLifeCardDownloadBugs( self, event ):
		event.Skip()
	
	def OnButtonClearLog( self, event ):
		event.Skip()
	
	def OnButtonClickExit( self, event ):
		event.Skip()
	
	def OnButtonClickClearRegistry( self, event ):
		event.Skip()
	

###########################################################################
## Class DialogLongOp
###########################################################################

class DialogLongOp ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer21 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticTextMessage = wx.StaticText( self, wx.ID_ANY, u"The operation is long and messages will be displayed in the log\nunderneath.\n\nPlease do not close this dialog box until the operation has either\nbeen completed or interrupted due to an error", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextMessage.Wrap( -1 )
		bSizer21.Add( self.m_staticTextMessage, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		self.m_button13 = wx.Button( self, wx.ID_ANY, u"Ok", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer21.Add( self.m_button13, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer21 )
		self.Layout()
		bSizer21.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button13.Bind( wx.EVT_BUTTON, self.OnButonClickOk )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnButonClickOk( self, event ):
		event.Skip()
	

