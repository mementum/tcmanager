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
import openpyxl
import xlsxwriter

class XlsxWriter(object):

    def __init__(self):
        self.wb = None

    def Workbook(self, filename):
        self.wb = xlsxWriter.Workbook(filename, {'constant_memory': True})
        return self

    def Close(self):
        if self.wb:
            self.wb.close()


    def NewWorksheet(self, sheetname=''):
        


    def __del__(self):
        if self.wb:
            self.wb.close()





ExcelWriter = XlsxWriter
