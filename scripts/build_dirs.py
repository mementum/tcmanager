#!/usr/bin/env python
# -*- coding: utf-8; py-indent-offset:4 -*-
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
import os.path
import sys


def add_dir_rel(dirname, path, start):
    dirpath = os.path.relpath(path, start)
    setattr(thismod, dirname, dirpath)

def add_dir(dirname, dirpath, dirext=''):
    if dirext:
        dirpath = os.path.join(dirpath, dirext)
    setattr(thismod, dirname, dirpath)

thismod = sys.modules[__name__]

add_dir('scriptdir', os.path.dirname(sys.argv[0]))
add_dir('hooksdir', scriptdir, 'hooks')

add_dir('basedir', scriptdir, '..')
add_dir('srcdir', basedir, 'src')
add_dir('builddir', basedir, 'build')
add_dir('distdir', basedir, 'dist')

add_dir('setupdistdir', distdir, 'inno')
add_dir('setupbuilddir', builddir, 'inno')

# Inno Setup needs relative paths to the script
add_dir_rel('relsetupbuild', setupbuilddir, scriptdir)
add_dir_rel('relsetupdist', setupdistdir, scriptdir)
