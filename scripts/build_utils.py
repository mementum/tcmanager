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
import fnmatch, glob, imp, os, os.path, shutil, sys, tempfile
#
# Line buffering is broken in Win32 platforms
# Running under cygwin/mingw32 this is needed to see a line
# show up when the print statement is issued
class flushfile(object):
    def __init__(self, f):
        self.f = f

    def write(self, x):
        self.f.write(x)
        self.f.flush()

if sys.platform == 'win32':
    sys.stdout = flushfile(sys.stdout)
    sys.stderr = flushfile(sys.stderr)


def locate_single_file(dirname, pattern):
    pfiles = glob.glob(os.path.join(dirname, pattern))
    return (pfiles[0], pfiles) if len(pfiles) == 1 else (None, None)

def delete_files(pathname, patterns):
    for dirpath, dirs, files in os.walk(pathname): 
        files_to_remove = list()
        for pattern in patterns:
            files_to_remove.extend(fnmatch.filter(files, pattern))

        for file in files_to_remove:
            path_to_remove = os.path.join(dirpath, file)
            print 'Removing file:', path_to_remove
            os.remove(path_to_remove)

def del_dir_if_exists(dirname, redo=False):
    if os.path.isdir(dirname):
        print '-- Removing:', dirname
        shutil.rmtree(dirname)

    if redo:
        os.mkdir(dirname)

def cp_r(src, dst):
    if os.path.isfile(src):
        shutil.copy(src, dst)
    elif os.path.isdir(src):
        shutil.copytree(src, dst)
    else:
        raise Exception('Unknown file/dir type for cp_r')

def cp_r_below_dir(srcdir, dstdir, pattern):

    below_dir = glob.glob(os.path.join(srcdir, pattern))
    for src in below_dir:
        dst = os.path.join(dstdir, os.path.basename(src))
        cp_r(src, dst)


def load_module(modname, path):
    try:
        foundmodule = imp.find_module(modname, [path,])
    except Exception, e:
        raise e

    try:
        loadedmodule = imp.load_module(modname, *foundmodule)
    except Exception, e:
        raise e

    return loadedmodule


def replace_in_file(ifilepath, callback, *args):
    #Create temp file
    ofilehandle, ofilepath = tempfile.mkstemp() # open temporary file
    ofile = os.fdopen(ofilehandle, 'w')  # wrap fhandle in "file object"
    ifile = open(ifilepath) # open original file
    for line in ifile:
        line = callback(line, *args)
        ofile.write(line)

    ofile.close() # close temp file
    ifile.close() # close original file
    os.remove(ifilepath) # remove original file
    shutil.move(ofilepath, ifilepath) # move new file
