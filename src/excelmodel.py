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

import xlrd
import xlwt.Utils

class ExcelInput(object):

    def __init__(self, workbookname):
        self.workbook = xlrd.open_workbook(workbookname)


    def get_lifecard_updates(self, wksheetname, row_start, ticket_col, resol_col, comment_col):
        wksheet = self.workbook.sheet_by_name(wksheetname)

        updates = OrderedDict()

        ticket_col = xlwt.Utils.col_by_name(ticket_col)
        resol_col = xlwt.Utils.col_by_name(resol_col)
        comment_col = xlwt.Utils.col_by_name(comment_col)
        row = int(row_start) -1
        while True:
            try:
                ticket_id = int(wksheet.cell_value(row, ticket_col))
            except IndexError, e:
                if row >= wksheet.nrows:
                    # expected limit reached
                    break
                raise e # something else, reraise
            except Exception, e:
                raise e # something, reraise

            resolution = wksheet.cell_value(row, resol_col)
            comment = wksheet.cell_value(row, comment_col)
            if resolution or comment:
                updates[ticket_id] = (resolution, comment)
            row += 1

        return updates


        
