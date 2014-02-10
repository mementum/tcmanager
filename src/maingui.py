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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Test Case Manager", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel6 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer16 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_notebook1 = wx.Notebook( self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.NB_BOTTOM )
		self.m_panel8 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer12 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer12 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel8, wx.ID_ANY, u"Server Details" ), wx.VERTICAL )
		
		fgSizer5 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer5.AddGrowableCol( 1 )
		fgSizer5.AddGrowableCol( 3 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText7 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"Server Url", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		fgSizer5.Add( self.m_staticText7, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer431 = wx.BoxSizer( wx.HORIZONTAL )
		
		m_comboBoxServerUrlChoices = []
		self.m_comboBoxServerUrl = wx.ComboBox( self.m_panel8, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_comboBoxServerUrlChoices, wx.CB_DROPDOWN|wx.CB_SORT )
		bSizer431.Add( self.m_comboBoxServerUrl, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_button202 = wx.Button( self.m_panel8, wx.ID_ANY, u"Del Url", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button202.Enable( False )
		
		bSizer431.Add( self.m_button202, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		fgSizer5.Add( bSizer431, 1, wx.EXPAND, 5 )
		
		self.m_staticText25 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )
		fgSizer5.Add( self.m_staticText25, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer44 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_textCtrlServerUsername = wx.TextCtrl( self.m_panel8, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer44.Add( self.m_textCtrlServerUsername, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_button211 = wx.Button( self.m_panel8, wx.ID_ANY, u"Del Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer44.Add( self.m_button211, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		fgSizer5.Add( bSizer44, 0, 0, 5 )
		
		self.m_staticText4 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		fgSizer5.Add( self.m_staticText4, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
		
		bSizer45 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_panel5 = wx.Panel( self.m_panel8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer181 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_textCtrlServerPassword = wx.TextCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		bSizer181.Add( self.m_textCtrlServerPassword, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrlServerPasswordShown = wx.TextCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrlServerPasswordShown.Hide()
		
		bSizer181.Add( self.m_textCtrlServerPasswordShown, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		self.m_panel5.SetSizer( bSizer181 )
		self.m_panel5.Layout()
		bSizer181.Fit( self.m_panel5 )
		bSizer45.Add( self.m_panel5, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_checkBoxServerPasswordShow = wx.CheckBox( self.m_panel8, wx.ID_ANY, u"Show Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer45.Add( self.m_checkBoxServerPasswordShow, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		fgSizer5.Add( bSizer45, 1, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		sbSizer12.Add( fgSizer5, 1, wx.EXPAND, 5 )
		
		self.m_staticline32 = wx.StaticLine( self.m_panel8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		sbSizer12.Add( self.m_staticline32, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer46 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer46.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_button10 = wx.Button( self.m_panel8, wx.ID_ANY, u"Test Server Connection", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button10.Enable( False )
		
		bSizer46.Add( self.m_button10, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_checkBox6 = wx.CheckBox( self.m_panel8, wx.ID_ANY, u"Check Server Connection on Start", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox6.Enable( False )
		
		bSizer46.Add( self.m_checkBox6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer46.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		sbSizer12.Add( bSizer46, 0, wx.EXPAND, 5 )
		
		
		bSizer12.Add( sbSizer12, 0, wx.EXPAND, 5 )
		
		sbSizer6 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel8, wx.ID_ANY, u"Test Catalogs" ), wx.VERTICAL )
		
		bSizer52 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText151 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"Available Catalogs", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText151.Wrap( -1 )
		bSizer52.Add( self.m_staticText151, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_choiceCatalogsChoices = []
		self.m_choiceCatalogs = wx.Choice( self.m_panel8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choiceCatalogsChoices, 0 )
		self.m_choiceCatalogs.SetSelection( 0 )
		bSizer52.Add( self.m_choiceCatalogs, 1, wx.ALL, 5 )
		
		self.m_button16 = wx.Button( self.m_panel8, wx.ID_ANY, u"Refresh", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer52.Add( self.m_button16, 0, wx.TOP|wx.RIGHT|wx.LEFT, 5 )
		
		
		sbSizer6.Add( bSizer52, 0, wx.EXPAND, 5 )
		
		bSizer22 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button14 = wx.Button( self.m_panel8, wx.ID_ANY, u"Delete Selected", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer22.Add( self.m_button14, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_button15 = wx.Button( self.m_panel8, wx.ID_ANY, u"Delete All", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer22.Add( self.m_button15, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		sbSizer6.Add( bSizer22, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer12.Add( sbSizer6, 0, wx.EXPAND|wx.TOP, 5 )
		
		
		self.m_panel8.SetSizer( bSizer12 )
		self.m_panel8.Layout()
		bSizer12.Fit( self.m_panel8 )
		self.m_notebook1.AddPage( self.m_panel8, u"Configuration", True )
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
		self.m_checkBoxUploadUpdateTc.Enable( False )
		
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
		
		bSizer31 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_checkBoxDownloadExcelNotSave = wx.CheckBox( self.m_panel7, wx.ID_ANY, u"Don't save", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer31.Add( self.m_checkBoxDownloadExcelNotSave, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticline24 = wx.StaticLine( self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer31.Add( self.m_staticline24, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_checkBoxDownloadKeepExcelOpen = wx.CheckBox( self.m_panel7, wx.ID_ANY, u"Keep open", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer31.Add( self.m_checkBoxDownloadKeepExcelOpen, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		
		bSizer31.AddSpacer( ( 0, 0), 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticline44 = wx.StaticLine( self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer31.Add( self.m_staticline44, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_checkBoxLcDownMakeCopy = wx.CheckBox( self.m_panel7, wx.ID_ANY, u"Make Copy (Prepend Date - Append CW)", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer31.Add( self.m_checkBoxLcDownMakeCopy, 0, wx.TOP|wx.BOTTOM|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		fgSizer211.Add( bSizer31, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		
		fgSizer211.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticline55 = wx.StaticLine( self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer211.Add( self.m_staticline55, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		fgSizer211.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		bSizer43 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_checkBoxLcDownFilterVendorComments = wx.CheckBox( self.m_panel7, wx.ID_ANY, u"Filter Vendor Comments", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer43.Add( self.m_checkBoxLcDownFilterVendorComments, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticline441 = wx.StaticLine( self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer43.Add( self.m_staticline441, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText37 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"and", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText37.Wrap( -1 )
		bSizer43.Add( self.m_staticText37, 0, wx.ALL, 5 )
		
		self.m_checkBoxLcDownCopyWithVendorComments = wx.CheckBox( self.m_panel7, wx.ID_ANY, u"Make Copy with Vendor Comments", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer43.Add( self.m_checkBoxLcDownCopyWithVendorComments, 0, wx.ALL, 5 )
		
		
		fgSizer211.Add( bSizer43, 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		fgSizer211.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticline261 = wx.StaticLine( self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer211.Add( self.m_staticline261, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText241 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Download States", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText241.Wrap( -1 )
		fgSizer211.Add( self.m_staticText241, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer402 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_checkBoxDownloadOpen = wx.CheckBox( self.m_panel7, wx.ID_ANY, u"Open", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer402.Add( self.m_checkBoxDownloadOpen, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticline122 = wx.StaticLine( self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer402.Add( self.m_staticline122, 0, wx.EXPAND|wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_checkBoxDownloadClosed = wx.CheckBox( self.m_panel7, wx.ID_ANY, u"Closed", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer402.Add( self.m_checkBoxDownloadClosed, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticline123 = wx.StaticLine( self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer402.Add( self.m_staticline123, 0, wx.EXPAND|wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_checkBoxDownloadInvestigation = wx.CheckBox( self.m_panel7, wx.ID_ANY, u"Investigation", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer402.Add( self.m_checkBoxDownloadInvestigation, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticline1231 = wx.StaticLine( self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer402.Add( self.m_staticline1231, 0, wx.EXPAND|wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_checkBoxDownloadFixed = wx.CheckBox( self.m_panel7, wx.ID_ANY, u"Fixed", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer402.Add( self.m_checkBoxDownloadFixed, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer402.AddSpacer( ( 0, 0), 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticline12 = wx.StaticLine( self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer402.Add( self.m_staticline12, 0, wx.EXPAND|wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_checkBoxDownloadRejected = wx.CheckBox( self.m_panel7, wx.ID_ANY, u"Rejected", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer402.Add( self.m_checkBoxDownloadRejected, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer402.AddSpacer( ( 0, 0), 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticline121 = wx.StaticLine( self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer402.Add( self.m_staticline121, 0, wx.EXPAND|wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_checkBoxDownloadNew = wx.CheckBox( self.m_panel7, wx.ID_ANY, u"New", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer402.Add( self.m_checkBoxDownloadNew, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		fgSizer211.Add( bSizer402, 1, wx.EXPAND, 5 )
		
		self.m_staticline22 = wx.StaticLine( self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer211.Add( self.m_staticline22, 0, wx.EXPAND|wx.TOP|wx.BOTTOM|wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticline221 = wx.StaticLine( self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer211.Add( self.m_staticline221, 0, wx.EXPAND|wx.TOP|wx.BOTTOM|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText16 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Attachment Dir", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )
		fgSizer211.Add( self.m_staticText16, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer53 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_dirPickerDirAttachments = wx.DirPickerCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		bSizer53.Add( self.m_dirPickerDirAttachments, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		
		fgSizer211.Add( bSizer53, 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		fgSizer211.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticline56 = wx.StaticLine( self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer211.Add( self.m_staticline56, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText32 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Download Attachments", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )
		fgSizer211.Add( self.m_staticText32, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		bSizer41 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_checkBoxLcDownAttachOpen = wx.CheckBox( self.m_panel7, wx.ID_ANY, u"Open", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer41.Add( self.m_checkBoxLcDownAttachOpen, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticline3111 = wx.StaticLine( self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer41.Add( self.m_staticline3111, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_checkBoxLcDownAttachClosed = wx.CheckBox( self.m_panel7, wx.ID_ANY, u"Closed", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer41.Add( self.m_checkBoxLcDownAttachClosed, 0, wx.ALL, 5 )
		
		self.m_staticline311 = wx.StaticLine( self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer41.Add( self.m_staticline311, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_checkBoxLcDownAttachInvestigation = wx.CheckBox( self.m_panel7, wx.ID_ANY, u"Investigation", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer41.Add( self.m_checkBoxLcDownAttachInvestigation, 0, wx.ALL, 5 )
		
		self.m_staticline3112 = wx.StaticLine( self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer41.Add( self.m_staticline3112, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_checkBoxLcDownAttachFixed = wx.CheckBox( self.m_panel7, wx.ID_ANY, u"Fixed", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer41.Add( self.m_checkBoxLcDownAttachFixed, 0, wx.ALL, 5 )
		
		
		bSizer41.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticline31121 = wx.StaticLine( self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer41.Add( self.m_staticline31121, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_checkBoxLcDownAttachRejected = wx.CheckBox( self.m_panel7, wx.ID_ANY, u"Rejected", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer41.Add( self.m_checkBoxLcDownAttachRejected, 0, wx.ALL, 5 )
		
		
		bSizer41.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticline311211 = wx.StaticLine( self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer41.Add( self.m_staticline311211, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_checkBoxLcDownAttachNew = wx.CheckBox( self.m_panel7, wx.ID_ANY, u"New", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer41.Add( self.m_checkBoxLcDownAttachNew, 0, wx.ALL, 5 )
		
		
		fgSizer211.Add( bSizer41, 0, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		
		bSizer24.Add( fgSizer211, 0, wx.EXPAND, 5 )
		
		self.m_staticline30 = wx.StaticLine( self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer24.Add( self.m_staticline30, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer26 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button20 = wx.Button( self.m_panel7, wx.ID_ANY, u"Download TestCases to LifeCard", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer26.Add( self.m_button20, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_button17 = wx.Button( self.m_panel7, wx.ID_ANY, u"Download Attachments", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer26.Add( self.m_button17, 0, wx.ALL, 5 )
		
		
		bSizer24.Add( bSizer26, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.BOTTOM, 5 )
		
		
		self.m_panel7.SetSizer( bSizer24 )
		self.m_panel7.Layout()
		bSizer24.Fit( self.m_panel7 )
		self.m_notebook1.AddPage( self.m_panel7, u"LifeCard Download", False )
		self.m_panel71 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer241 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer9 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel71, wx.ID_ANY, u"LifeCard Details" ), wx.VERTICAL )
		
		bSizer32 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText9111 = wx.StaticText( self.m_panel71, wx.ID_ANY, u"Filename", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9111.Wrap( -1 )
		bSizer32.Add( self.m_staticText9111, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_filePickerLifeCardExcelUp = wx.FilePickerCtrl( self.m_panel71, wx.ID_ANY, wx.EmptyString, u"Select a file", u"Excel Files (*.xlsx;*.xls)|*.xlsx;*.xls|All Files (*.*)|*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_CHANGE_DIR|wx.FLP_FILE_MUST_EXIST|wx.FLP_OPEN|wx.FLP_USE_TEXTCTRL )
		bSizer32.Add( self.m_filePickerLifeCardExcelUp, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		sbSizer9.Add( bSizer32, 0, wx.EXPAND, 5 )
		
		self.m_staticline31 = wx.StaticLine( self.m_panel71, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		sbSizer9.Add( self.m_staticline31, 0, wx.EXPAND |wx.ALL, 5 )
		
		gSizer1 = wx.GridSizer( 0, 3, 0, 0 )
		
		bSizer33 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText24 = wx.StaticText( self.m_panel71, wx.ID_ANY, u"Sheet Name", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.m_staticText24.Wrap( -1 )
		bSizer33.Add( self.m_staticText24, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrlLifeCardUpSheetName = wx.TextCtrl( self.m_panel71, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer33.Add( self.m_textCtrlLifeCardUpSheetName, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		gSizer1.Add( bSizer33, 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer331 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText91111 = wx.StaticText( self.m_panel71, wx.ID_ANY, u"Ticket Id Col", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.m_staticText91111.Wrap( -1 )
		bSizer331.Add( self.m_staticText91111, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrlLifeCardUpColTicketId = wx.TextCtrl( self.m_panel71, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer331.Add( self.m_textCtrlLifeCardUpColTicketId, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		gSizer1.Add( bSizer331, 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer3311 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer3311.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		gSizer1.Add( bSizer3311, 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer40 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText23 = wx.StaticText( self.m_panel71, wx.ID_ANY, u"Start Row", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.m_staticText23.Wrap( -1 )
		bSizer40.Add( self.m_staticText23, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrlLifeCardUpRowStart = wx.TextCtrl( self.m_panel71, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer40.Add( self.m_textCtrlLifeCardUpRowStart, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		gSizer1.Add( bSizer40, 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer401 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText21 = wx.StaticText( self.m_panel71, wx.ID_ANY, u"Resolution Col", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.m_staticText21.Wrap( -1 )
		bSizer401.Add( self.m_staticText21, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrlLifeCardUpColResolution = wx.TextCtrl( self.m_panel71, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer401.Add( self.m_textCtrlLifeCardUpColResolution, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		gSizer1.Add( bSizer401, 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer4011 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText22 = wx.StaticText( self.m_panel71, wx.ID_ANY, u"Comment Col", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.m_staticText22.Wrap( -1 )
		bSizer4011.Add( self.m_staticText22, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrlLifeCardUpColComment = wx.TextCtrl( self.m_panel71, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4011.Add( self.m_textCtrlLifeCardUpColComment, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		gSizer1.Add( bSizer4011, 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		sbSizer9.Add( gSizer1, 1, wx.EXPAND, 5 )
		
		
		bSizer241.Add( sbSizer9, 0, wx.EXPAND, 5 )
		
		sbSizer10 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel71, wx.ID_ANY, u"Allow Updates on Ticket Status" ), wx.HORIZONTAL )
		
		self.m_checkBoxLifeCardUpStatusOpen = wx.CheckBox( self.m_panel71, wx.ID_ANY, u"Open", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer10.Add( self.m_checkBoxLifeCardUpStatusOpen, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticline18 = wx.StaticLine( self.m_panel71, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		sbSizer10.Add( self.m_staticline18, 0, wx.EXPAND|wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_checkBoxLifeCardUpStatusClosed = wx.CheckBox( self.m_panel71, wx.ID_ANY, u"Closed", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer10.Add( self.m_checkBoxLifeCardUpStatusClosed, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticline181 = wx.StaticLine( self.m_panel71, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		sbSizer10.Add( self.m_staticline181, 0, wx.EXPAND|wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_checkBoxLifeCardUpStatusInvestigation = wx.CheckBox( self.m_panel71, wx.ID_ANY, u"Investigation", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer10.Add( self.m_checkBoxLifeCardUpStatusInvestigation, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticline1811 = wx.StaticLine( self.m_panel71, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		sbSizer10.Add( self.m_staticline1811, 0, wx.EXPAND|wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_checkBoxLifeCardUpStatusFixed = wx.CheckBox( self.m_panel71, wx.ID_ANY, u"Fixed", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer10.Add( self.m_checkBoxLifeCardUpStatusFixed, 0, wx.ALL, 5 )
		
		
		sbSizer10.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticline18111 = wx.StaticLine( self.m_panel71, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		sbSizer10.Add( self.m_staticline18111, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_checkBoxLifeCardUpStatusRejected = wx.CheckBox( self.m_panel71, wx.ID_ANY, u"Rejected", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer10.Add( self.m_checkBoxLifeCardUpStatusRejected, 0, wx.ALL, 5 )
		
		
		sbSizer10.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticline181111 = wx.StaticLine( self.m_panel71, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		sbSizer10.Add( self.m_staticline181111, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_checkBoxLifeCardUpStatusNew = wx.CheckBox( self.m_panel71, wx.ID_ANY, u"New", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer10.Add( self.m_checkBoxLifeCardUpStatusNew, 0, wx.ALL, 5 )
		
		
		bSizer241.Add( sbSizer10, 0, wx.EXPAND, 5 )
		
		sbSizer11 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel71, wx.ID_ANY, u"Vendor Name" ), wx.HORIZONTAL )
		
		self.m_textCtrlLifeCardAuthorUp = wx.TextCtrl( self.m_panel71, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer11.Add( self.m_textCtrlLifeCardAuthorUp, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText29 = wx.StaticText( self.m_panel71, wx.ID_ANY, u"To use on the web system for updates sent by the vendor", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText29.Wrap( -1 )
		sbSizer11.Add( self.m_staticText29, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer241.Add( sbSizer11, 0, wx.EXPAND, 5 )
		
		bSizer261 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button201 = wx.Button( self.m_panel71, wx.ID_ANY, u"Upload", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer261.Add( self.m_button201, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer241.Add( bSizer261, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.m_panel71.SetSizer( bSizer241 )
		self.m_panel71.Layout()
		bSizer241.Fit( self.m_panel71 )
		self.m_notebook1.AddPage( self.m_panel71, u"LifeCard Upload", False )
		
		bSizer16.Add( self.m_notebook1, 1, wx.EXPAND, 5 )
		
		self.m_staticline8 = wx.StaticLine( self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer16.Add( self.m_staticline8, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer10 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText5 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Operations Log", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		bSizer10.Add( self.m_staticText5, 0, wx.ALL, 5 )
		
		self.m_textCtrlLog = wx.TextCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 600,250 ), wx.TE_MULTILINE|wx.TE_READONLY )
		bSizer10.Add( self.m_textCtrlLog, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button7 = wx.Button( self.m_panel6, wx.ID_ANY, u"Clear Log", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_button7, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_button6 = wx.Button( self.m_panel6, wx.ID_ANY, u"Exit", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_button6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_button5 = wx.Button( self.m_panel6, wx.ID_ANY, u"Clear Registry", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_button5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_button191 = wx.Button( self.m_panel6, wx.ID_ANY, u"Reset Window Size", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_button191, 0, wx.ALL, 5 )
		
		
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
		self.Bind( wx.EVT_SIZE, self.OnSizeMainFrame )
		self.m_comboBoxServerUrl.Bind( wx.EVT_COMBOBOX, self.OnComboboxServerUrl )
		self.m_comboBoxServerUrl.Bind( wx.EVT_KILL_FOCUS, self.OnKillFocusComboboxServerUrl )
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
		self.m_checkBoxDownloadExcelNotSave.Bind( wx.EVT_CHECKBOX, self.OnCheckBoxDownloadExcelNotSave )
		self.m_checkBoxDownloadKeepExcelOpen.Bind( wx.EVT_CHECKBOX, self.OnCheckBoxDownloadKeepExcelOpen )
		self.m_checkBoxLcDownMakeCopy.Bind( wx.EVT_CHECKBOX, self.OnCheckBoxLcDownMakeCopy )
		self.m_checkBoxLcDownFilterVendorComments.Bind( wx.EVT_CHECKBOX, self.OnCheckBoxLcDownFilterVendorComments )
		self.m_checkBoxLcDownCopyWithVendorComments.Bind( wx.EVT_CHECKBOX, self.OnCheckBoxLcDownCopyWithVendorComments )
		self.m_checkBoxDownloadOpen.Bind( wx.EVT_CHECKBOX, self.OnCheckBoxDownloadOpen )
		self.m_checkBoxDownloadClosed.Bind( wx.EVT_CHECKBOX, self.OnCheckBoxDownloadClosed )
		self.m_checkBoxDownloadInvestigation.Bind( wx.EVT_CHECKBOX, self.OnCheckBoxDownloadInvestigation )
		self.m_checkBoxDownloadFixed.Bind( wx.EVT_CHECKBOX, self.OnCheckBoxDownloadFixed )
		self.m_checkBoxDownloadRejected.Bind( wx.EVT_CHECKBOX, self.OnCheckBoxDownloadRejected )
		self.m_checkBoxDownloadNew.Bind( wx.EVT_CHECKBOX, self.OnCheckBoxDownloadNew )
		self.m_dirPickerDirAttachments.Bind( wx.EVT_DIRPICKER_CHANGED, self.OnDirChangedDirAttachments )
		self.m_checkBoxLcDownAttachOpen.Bind( wx.EVT_CHECKBOX, self.OnCheckBoxLcDownAttachOpen )
		self.m_checkBoxLcDownAttachClosed.Bind( wx.EVT_CHECKBOX, self.OnCheckBoxLcDownAttachClosed )
		self.m_checkBoxLcDownAttachInvestigation.Bind( wx.EVT_CHECKBOX, self.OnCheckBoxLcDownAttachInvestigation )
		self.m_checkBoxLcDownAttachFixed.Bind( wx.EVT_CHECKBOX, self.OnCheckBoxLcDownAttachFixed )
		self.m_checkBoxLcDownAttachRejected.Bind( wx.EVT_CHECKBOX, self.OnCheckBoxLcDownAttachRejected )
		self.m_checkBoxLcDownAttachNew.Bind( wx.EVT_CHECKBOX, self.OnCheckBoxLcDownAttachNew )
		self.m_button20.Bind( wx.EVT_BUTTON, self.OnButtonClickLifeCardDownload )
		self.m_button17.Bind( wx.EVT_BUTTON, self.OnButtonClickDownloadAttachments )
		self.m_filePickerLifeCardExcelUp.Bind( wx.EVT_FILEPICKER_CHANGED, self.OnFileChangedLifeCardExcelUp )
		self.m_textCtrlLifeCardUpSheetName.Bind( wx.EVT_KILL_FOCUS, self.OnKillFocusLifeCardUpSheetName )
		self.m_textCtrlLifeCardUpColTicketId.Bind( wx.EVT_KILL_FOCUS, self.OnKillFocusLifeCardUpColTicketId )
		self.m_textCtrlLifeCardUpRowStart.Bind( wx.EVT_KILL_FOCUS, self.OnKillFocusLifeCardUpColRowStart )
		self.m_textCtrlLifeCardUpColResolution.Bind( wx.EVT_KILL_FOCUS, self.OnKillFocusLifeCardUpColResolution )
		self.m_textCtrlLifeCardUpColComment.Bind( wx.EVT_KILL_FOCUS, self.OnKillFocusLifeCardUpColComment )
		self.m_checkBoxLifeCardUpStatusOpen.Bind( wx.EVT_CHECKBOX, self.OnCheckBoxLifeCardUpStatusOpen )
		self.m_checkBoxLifeCardUpStatusClosed.Bind( wx.EVT_CHECKBOX, self.OnCheckBoxLifeCardUpStatusClosed )
		self.m_checkBoxLifeCardUpStatusInvestigation.Bind( wx.EVT_CHECKBOX, self.OnCheckBoxLifeCardUpStatusInvestigation )
		self.m_checkBoxLifeCardUpStatusFixed.Bind( wx.EVT_CHECKBOX, self.OnCheckBoxLifeCardUpStatusFixed )
		self.m_checkBoxLifeCardUpStatusRejected.Bind( wx.EVT_CHECKBOX, self.OnCheckBoxLifeCardUpStatusRejected )
		self.m_checkBoxLifeCardUpStatusNew.Bind( wx.EVT_CHECKBOX, self.OnCheckBoxLifeCardUpStatusNew )
		self.m_textCtrlLifeCardAuthorUp.Bind( wx.EVT_KILL_FOCUS, self.OnKillFocuslLifeCardAuthorUp )
		self.m_staticText29.Bind( wx.EVT_KILL_FOCUS, self.OnKillFocusTicketUpdateAuthor )
		self.m_button201.Bind( wx.EVT_BUTTON, self.OnButtonClickLifeCardUpload )
		self.m_button7.Bind( wx.EVT_BUTTON, self.OnButtonClearLog )
		self.m_button6.Bind( wx.EVT_BUTTON, self.OnButtonClickExit )
		self.m_button5.Bind( wx.EVT_BUTTON, self.OnButtonClickClearRegistry )
		self.m_button191.Bind( wx.EVT_BUTTON, self.OnButtonClickResetSize )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnSizeMainFrame( self, event ):
		event.Skip()
	
	def OnComboboxServerUrl( self, event ):
		event.Skip()
	
	def OnKillFocusComboboxServerUrl( self, event ):
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
	
	def OnCheckBoxDownloadExcelNotSave( self, event ):
		event.Skip()
	
	def OnCheckBoxDownloadKeepExcelOpen( self, event ):
		event.Skip()
	
	def OnCheckBoxLcDownMakeCopy( self, event ):
		event.Skip()
	
	def OnCheckBoxLcDownFilterVendorComments( self, event ):
		event.Skip()
	
	def OnCheckBoxLcDownCopyWithVendorComments( self, event ):
		event.Skip()
	
	def OnCheckBoxDownloadOpen( self, event ):
		event.Skip()
	
	def OnCheckBoxDownloadClosed( self, event ):
		event.Skip()
	
	def OnCheckBoxDownloadInvestigation( self, event ):
		event.Skip()
	
	def OnCheckBoxDownloadFixed( self, event ):
		event.Skip()
	
	def OnCheckBoxDownloadRejected( self, event ):
		event.Skip()
	
	def OnCheckBoxDownloadNew( self, event ):
		event.Skip()
	
	def OnDirChangedDirAttachments( self, event ):
		event.Skip()
	
	def OnCheckBoxLcDownAttachOpen( self, event ):
		event.Skip()
	
	def OnCheckBoxLcDownAttachClosed( self, event ):
		event.Skip()
	
	def OnCheckBoxLcDownAttachInvestigation( self, event ):
		event.Skip()
	
	def OnCheckBoxLcDownAttachFixed( self, event ):
		event.Skip()
	
	def OnCheckBoxLcDownAttachRejected( self, event ):
		event.Skip()
	
	def OnCheckBoxLcDownAttachNew( self, event ):
		event.Skip()
	
	def OnButtonClickLifeCardDownload( self, event ):
		event.Skip()
	
	def OnButtonClickDownloadAttachments( self, event ):
		event.Skip()
	
	def OnFileChangedLifeCardExcelUp( self, event ):
		event.Skip()
	
	def OnKillFocusLifeCardUpSheetName( self, event ):
		event.Skip()
	
	def OnKillFocusLifeCardUpColTicketId( self, event ):
		event.Skip()
	
	def OnKillFocusLifeCardUpColRowStart( self, event ):
		event.Skip()
	
	def OnKillFocusLifeCardUpColResolution( self, event ):
		event.Skip()
	
	def OnKillFocusLifeCardUpColComment( self, event ):
		event.Skip()
	
	def OnCheckBoxLifeCardUpStatusOpen( self, event ):
		event.Skip()
	
	def OnCheckBoxLifeCardUpStatusClosed( self, event ):
		event.Skip()
	
	def OnCheckBoxLifeCardUpStatusInvestigation( self, event ):
		event.Skip()
	
	def OnCheckBoxLifeCardUpStatusFixed( self, event ):
		event.Skip()
	
	def OnCheckBoxLifeCardUpStatusRejected( self, event ):
		event.Skip()
	
	def OnCheckBoxLifeCardUpStatusNew( self, event ):
		event.Skip()
	
	def OnKillFocuslLifeCardAuthorUp( self, event ):
		event.Skip()
	
	def OnKillFocusTicketUpdateAuthor( self, event ):
		event.Skip()
	
	def OnButtonClickLifeCardUpload( self, event ):
		event.Skip()
	
	def OnButtonClearLog( self, event ):
		event.Skip()
	
	def OnButtonClickExit( self, event ):
		event.Skip()
	
	def OnButtonClickClearRegistry( self, event ):
		event.Skip()
	
	def OnButtonClickResetSize( self, event ):
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
	

