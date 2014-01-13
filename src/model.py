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
from collections import OrderedDict
import itertools
import threading

import openpyxl
import pythoncom
from win32com.client import Dispatch
import win32com.client.gencache
import xlrd
import xlsxwriter

from config import ConfigPrefix, ConfigString, ConfigBool
# from excelsupport import ExcelFile
from mvcbase import ModelRole, PubSend
from rpcsupport import RpcInterface
from tcmodel import TestCaseInPlan

@ModelRole
class Model(object):
    serverurl = ConfigString(name='serverurl', defvalue='')
    serverusername = ConfigString(name='server', defvalue='')
    serverpassword = ConfigString(name='serverpassword', defvalue='')

    uploadexcel = ConfigString(name='uploadexcel', defvalue='')
    uploadcatalogname = ConfigString(name='uploadcatalogname', defvalue='')
    uploadautosheets = ConfigBool(name='uploadautosheets', defvalue=False)
    uploadautocatalogs = ConfigBool(name='uploadautocatalogs', defvalue=False)

    uploadusecatalog = ConfigBool(name='uploadusecatalog', defvalue=False)
    uploadupdatetc = ConfigBool(name='uploadupdatetc', defvalue=False)

    downloadexcel = ConfigString(name='downloadexcel', defvalue='')

    lifecardexcel = ConfigString(name='lifecardexcel', defvalue='')
    lcovertestcases = ConfigBool(name='lcovertestcases', defvalue=False)

    def __init__(self):
        self.serverpasswordshow = False

        self.uploadsheets = list()
        self.uploadsheet = None

        self.catalogs = list()
        self.downloadcatalog = None

        self.lifecardcatalog = None
        self.lifecardtestplan = None


    @PubSend('logappend')
    def LogAppend(self, msg):
        return msg

    @PubSend('init')
    def init(self):
        return None

    @PubSend('uploadsheets')
    def GetUploadSheets(self):
        self.uploadsheets[:] = []
        wkbook = openpyxl.load_workbook(self.uploadexcel, use_iterators=True)
        self.uploadsheets = wkbook.get_sheet_names()

    @PubSend('catalogs')
    def GetUploadCatalogs(self):
        self.catalogs[:] = []
        rpc = RpcInterface(self.serverurl, self.serverusername, self.serverpassword)
        self.catalogs = rpc.listSubCatalogsExt('')

    @PubSend('catalogdeleted')
    def DeleteCatalog(self, catalog):
        rpc = RpcInterface(self.serverurl, self.serverusername, self.serverpassword)
        self.LogAppend('Deleting Catalog %s' % catalog[0:3])
        rpc.deleteTestCatalog(catalog[0])
        self.LogAppend('Deleted Catalog %s' % catalog[0:3])
        return catalog

    @PubSend('catalogdeletedall')
    def DeleteCatalogAll(self):
        rpc = RpcInterface(self.serverurl, self.serverusername, self.serverpassword)
        self.LogAppend('Deleting All Catalogs')
        for catalog in self.catalogs:
            self.LogAppend('Deleting Catalog %s' % catalog[0:3])
            rpc.deleteTestCatalog(catalog[0])
            self.LogAppend('Deleted Catalog %s' % catalog[0:3])
        self.LogAppend('Deleted All Catalogs')

    #@PubSend('uploadingexcel')
    def UploadExcel(self):
        th = threading.Thread(target=self.UploadingExcel)
        th.start()

    @PubSend('uploadedexcel')
    def UploadingExcel(self):
        try:
            self.LogAppend('Using Excel file %s' % self.uploadexcel)
            # Open Workbook and sheet
            self.LogAppend('Opening excel file %s' % self.uploadexcel)
            workbook = xlrd.open_workbook(self.uploadexcel)
            chosensheet = self.uploadsheet
            self.LogAppend('Choosing sheet %s' % chosensheet)
            wksheet = workbook.sheet_by_name(chosensheet)

            self.LogAppend('Parsing TestCases Fields and categories, to create subcatalogs')
            headerfields = dict()
            catcols = 0
            tcdescription = 'Test Case Fields'
            row = 0
            while True:
                try:
                    cellvalue = wksheet.cell_value(row, catcols)
                except IndexError, e:
                    if catcols >= wksheet.ncols:
                        # expected limit reached
                        break
                    raise e
                except Exception, e:
                    raise e

                if not cellvalue:
                    break
                headerfields[catcols] = cellvalue
                tcdescription += ':%s' % cellvalue
                catcols += 1

            self.LogAppend('Excel header has %d columns' % catcols)
            self.LogAppend('Header names %s' % str(headerfields).strip('[]'))

            self.LogAppend('Creating Catalog %s' % self.uploadcatalogname)
            rpcinterface = RpcInterface(self.serverurl, self.serverusername, self.serverpassword)
            rootid = rpcinterface.createTestCatalog('', self.uploadcatalogname, tcdescription)
            self.LogAppend('Created Catalog with id %s' % rootid)

            # Parse the Category and subcategory columns
            categories = dict()
            while True:
                colidx = itertools.count()
                row += 1
                try:
                    maincat = wksheet.cell_value(row, colidx.next())
                except IndexError, e:
                    if row >= wksheet.nrows:
                        maincat = None # expected limit reached
                    else:
                        raise e # unexpected ... let's see it
                except Exception, e:
                    raise e # unexpected ... let's see it

                if not maincat: # if row >= wksheet.nrows
                    self.LogAppend('End of TestCases')
                    break # end of testcases

                # Get the main category (create if needed as child of root)
                if maincat not in categories:
                    self.LogAppend('Creating SubCatalog %s' % maincat)
                    catid = rpcinterface.createTestCatalog(rootid, maincat, '')

                    categories[maincat] = catid
                    self.LogAppend('Created SubCatalog %s with id %s' % (maincat, catid))
                else:
                    self.LogAppend('Next Testcase - Category %s' % maincat)
                    catid = categories[maincat]

                # Get the sub category (create if needed as child of main category)
                subcat = wksheet.cell_value(row, colidx.next())
                if subcat:
                    subcatkey = '%s::%s' % (maincat, subcat)
                    if subcatkey not in categories:
                        self.LogAppend('Creating SubSubCatalog %s' % subcat)
                        catid = rpcinterface.createTestCatalog(catid, subcat, '')

                        categories[subcatkey] = catid
                        self.LogAppend('Created SubSubCatalog %s with id %s' % (subcat, catid))
                    else:
                        self.LogAppend('Next Testcase - Category %s' % subcatkey)
                        catid = categories[subcatkey]

                # Get the title
                tctitle = wksheet.cell_value(row, colidx.next())

                # Get Description and complete
                tcdesc = wksheet.cell_value(row, colidx.next())
                for col in xrange(colidx.next(), catcols):
                    tcdesc += '\n\n'
                    tcdesc += '== %s ==\n' % headerfields[col]
                    cellvalue = wksheet.cell_value(row, col)
                    celltype = wksheet.cell_type(row, col)
                    if celltype != xlrd.XL_CELL_TEXT:
                        cellvalue = str(cellvalue)
                    tcdesc += cellvalue
                    tcdesc += '\n\n'

                # Testcase is complete and we have a cat id
                self.LogAppend('Creating testcase %d with title %s' % (row, tctitle))
                tcid = rpcinterface.createTestCase(catid, tctitle, tcdesc)

                self.LogAppend('%d TestCase create (id %s/catalog id %s)' % (row, tcid, catid))

        except Exception, e:
            self.LogAppend('Error during excel upload: %s' % str(e))

        self.GetUploadCatalogs()


    #@PubSend('downloadingexcel')
    def DownloadExcel(self):
        th = threading.Thread(target=self.DownloadingExcel)
        th.start()

    @PubSend('downloadedexcel')
    def DownloadingExcel(self):
        try:
            self.LogAppend('Downloading Catalog to Excel')
            self.LogAppend('Preparing root catalog')
            rootcat = self.downloadcatalog
            rootid = rootcat[0]

            # Prepare for Excel
            sheetname = rootcat[2]
            if not sheetname:
                self.LogAppend('Catalog has no name, using "Test Catalog" for the Excel Tab')
                sheetname = 'Test Catalog'
            else:
                self.LogAppend('Excel Tab: %s' % sheetname)

            # Open Excel
            # wkbook = openpyxl.reader.excel.load_workbook(self.downloadexcel)
            self.LogAppend('Opening a workbook in memory')
            wkbook = openpyxl.Workbook()
            self.LogAppend('Creating the tab')
            # wksheet = wkbook.create_sheet(title=sheetname)
            wksheet = wkbook.get_active_sheet()
            wksheet.title = sheetname

            # Connect to Server
            self.LogAppend('Creating an RPC interface to the server')
            rpcinterface = RpcInterface(self.serverurl, self.serverusername, self.serverpassword)

            # FIXME: I am getting the full catalog from the interface
            if False:
                rootcat = rpcinterface.getTestCatalog(rootid)
                rootcat.insert(0, rootid) # use to create a full hierarcha of catalogs
            self.LogAppend('Preparing root catalog and headers')
            catalogs = [rootcat]
            catdesc = rootcat[3]
            headers = catdesc.split(':')[1:]

            row = 0
            for col, header in enumerate(headers):
                wksheet.cell(row=row, column=col).value = header

            self.LogAppend('Start testcases export')
            tt2category = dict()
            # Go for it
            while catalogs:
                nextcatalogs = list()
                self.LogAppend('Iterating over %d catalogs' % len(catalogs))
                for catalog in catalogs:
                    self.LogAppend('Exploring catalog %s' % str(catalog))
                    tt2category[catalog[0]] = catalog[2] # map id to category (catalog name)

                    self.LogAppend('Getting subcatalogs of catalogs')
                    subcatalogs = rpcinterface.listSubCatalogs(catalog[0])
                    nextcatalogs.extend(subcatalogs)

                    self.LogAppend('Getting testcases of current catalog')
                    testcases = rpcinterface.listTestCases(catalog[0])
                    self.LogAppend('Iterating over %d testcases' % len(testcases))
                    for tc in testcases:
                        self.LogAppend('Exploring testcases %s' % str(tc[0:3]))
                        row += 1
                        colidx = itertools.count()
                        tctitle = tc[2]
                        tcdesc = tc[3]
                        # TC_TT0_TT1_TC32
                        # TC_TT0_TT1_TT2_TC33
                        tcname = tc[1]
                        txt = tcname[2:]
                        txt = txt.split('_TC')[0]
                        ttparts = txt.split('_TT')[1:]
                        category = ''
                        subcategory = ''

                        if len(ttparts) > 1:
                            category = tt2category[ttparts[1]]
                        if len(ttparts) > 2:
                            subcategory = tt2category[ttparts[2]]

                        self.LogAppend('Testcase in category/subcategory %s%s' % (category, subcategory))
                        self.LogAppend('Writing testcase to excel')

                        wksheet.cell(row=row, column=colidx.next()).value = category
                        wksheet.cell(row=row, column=colidx.next()).value = subcategory
                        wksheet.cell(row=row, column=colidx.next()).value = tctitle

                        self.LogAppend('Parsing testcase description')
                        tcdescparts = self.ParseDesc(tcdesc, headers)
                        self.LogAppend('Parsing testcase description got %d parts' % len(tcdescparts))
                        for desckey, descfield in tcdescparts.iteritems():
                            col = colidx.next()
                            wksheet.cell(row=row, column=col).set_value_explicit(descfield)
                            wksheet.cell(row=row, column=col).style.alignment.wrap_text = True

                self.LogAppend('End of testcases for current catalog')
                catalogs = nextcatalogs

            self.LogAppend('Saving Workbook to disk')
            wkbook.save(self.downloadexcel)
            self.LogAppend('Done Downloading to Excel')
        except Exception, e:
            self.LogAppend('Error during excel download: %s' % str(e))


    def ParseDesc(self, desc, headers, startcol=3):
        curheader = headers[startcol]
        parsed = OrderedDict([(curheader, '')])

        lines = desc.split('\n')
        for line in lines:
            if line.startswith('=='):
                # curheader = line.strip('\n= ')
                startcol += 1
                curheader = headers[startcol]
                parsed[curheader] = ''
            elif not line:
                continue
            else:
                parsed[curheader] += line + '\n'

        return parsed

    @PubSend('testplans')
    def GetTestPlans(self, catalog):
        rpc = RpcInterface(self.serverurl, self.serverusername, self.serverpassword)
        catid = catalog[0]
        testplans = rpc.listTestPlans(catid)
        return testplans

    #@PubSend('lifecarddownloadingexcel')
    def LifeCardDownloadExcel(self):
        th = threading.Thread(target=self.LifeCardDownloadingExcel)
        th.start()

    @PubSend('downloadedexcel')
    def LifeCardDownloadingExcel(self):
        custommap = {'comment': 1, 'tracefile': 2, 'testednetwork': 3}
        statusmap = {
            'to_be_tested': 'To Be Tested',
            'successful': 'Passed', 'passed': 'Passed',
            'failed': 'Failed',
            'skipped': 'Skipped', 'na': 'N/A', 'investigation': 'Investigation',
        }
        try:
            self.LogAppend('Compiling list of TestCases from server')
            self.LogAppend('Creating Workbook %s' % self.lifecardexcel)

            pythoncom.CoInitialize()
            # xl = Dispatch('Excel.Application')
            xl = win32com.client.gencache.EnsureDispatch ("Excel.Application")
            xl.Visible = 0
            wkbook = xl.Workbooks.Open(self.lifecardexcel)
            wksheet = wkbook.Sheets('Test Cases')
            wkscell = wksheet.Cells

            self.LogAppend('First Tab - Test Cases')
            self.LogAppend('Creating an RPC interface to the server')
            rpcinterface = RpcInterface(self.serverurl, self.serverusername, self.serverpassword)

            self.LogAppend('Start processing catalogs')
            self.LogAppend('Getting testcases of current catalog and testplan')
            tcips = rpcinterface.listTestCasesExt(self.lifecardcatalog[0], self.lifecardtestplan[0], True)
            self.LogAppend('Got %d testcases, processing them' % len(tcips))
            row = 4 # same as in lifecard
            coloffset = 6

            # Build a dict of the testcases for quick retrieval below
            tcipmap = dict(map(lambda x: (x[3], x), tcips))
            dcounter = itertools.count()
            xrows = itertools.count(4)
            for xrow in xrows:
                # tctitle = wksheet.Cells(xrow, 2).Value
                tctitle = wkscell(xrow, 3).Value
                if not tctitle:
                    break
                self.LogAppend('Filtering tcips against %s' % tctitle)
                try:
                    tcip = tcipmap[tctitle]
                except:
                    self.LogAppend('Testcase not found in dictionary. Default To Be Tested')
                    wkscell(row, coloffset + 0).Value = 'To Be Tested' # status
                    continue

                _tcip = TestCaseInPlan(tcip)
                self.LogAppend('Writing testcase %s' % _tcip.title)
                # wksheet.Cells(row, 5).Value = _tcip.title # title
                print statusmap[_tcip.status] # status
                wkscell(xrow, coloffset + 0).Value = statusmap[_tcip.status] # status
                for custfield in _tcip.customfields: # customfields
                    if custfield.name in custommap:
                        custcol = custommap[custfield.name]
                        custvalue = custfield.value
                        wkscell(xrow, coloffset + custcol).Value = custvalue

                    wkscell(xrow, coloffset + 4).Value = _tcip.author # timestamp
                    wkscell(xrow, coloffset + 5).Value =_tcip.timestamp.split('T')[0] # timestamp
                
            self.LogAppend('End downloading test-case-in-plan information')

        except Exception, e:
            self.LogAppend('Error during Download to LifeCard: %s' % str(e))

        if wkbook:
            wkbook.Save()
            wkbook.Close(False)
