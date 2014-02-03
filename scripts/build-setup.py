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
import os.path, subprocess, sys
import build_dirs, build_utils

iscc_cmd = ['iscc',]
scriptpattern = '*.iss'
appconstants = 'constants'

copy_items = {
    'basedir': ['README.md', 'LICENSE'],
    'srcdir': [],}

# Need to import constants
inno_replace = ['AppName', 'AppVersion', 'AppPublisher', 'AppYear', 'AppURL', 'AppExeName']
inno_dirs = {'BuildDir': build_dirs.relsetupbuild, 'DistDir': build_dirs.relsetupdist}

def replace_lines(line, loadedmodule):
    if line.startswith('#define'):
        # Do the replacement magic here
        define, defname, defvalue = line.strip('\r\n').split(None, 2)

        # check if defname is on the list of replacements
        # if yes replace using "" for the value
        # else write the original line
        defkey = defname[2:] # remove "My"

        if defkey in inno_replace:
            value = getattr(loadedmodule, defkey)
            line = ' '.join([define, defname, '"%s"' % value]) + '\n'
        elif defkey in inno_dirs:
            value = inno_dirs[defkey]
            line = ' '.join([define, defname, '"%s"' % value]) + '\n'

    return line

def pre_setup(modname, srcdir, setuppath):
    loadedmodule = build_utils.load_module(modname, srcdir)
    build_utils.replace_in_file(setuppath, replace_lines, loadedmodule)


if __name__ == '__main__':
    print '**-- Beginning of operations'

    print '-- Checking build/dist directories'
    build_utils.del_dir_if_exists(build_dirs.setupbuilddir, redo=True)
    build_utils.del_dir_if_exists(build_dirs.setupdistdir)

    print 'Copying distributable files'
    build_utils.cp_r_below_dir(build_dirs.distdir, build_dirs.setupbuilddir, '*')

    print 'Copying data files/directories to build directory'
    for dirname, items in copy_items.iteritems():
        for item in items:
            itempath = getattr(build_dirs, dirname)
            srcpath = os.path.join(itempath, item)
            dstpath = os.path.join(build_dirs.setupbuilddir, item)
            build_utils.cp_r(srcpath, dstpath)

    print 'Locating the innosetup iss file'
    issfile,issfiles = build_utils.locate_single_file(build_dirs.scriptdir, scriptpattern)
    if not issfile:
        print '-- ERROR: Found the following %s file(s): %s'  % (scriptpattern, issfiles)
        sys.exit(1)

    print 'Preparing iss file'
    pre_setup(appconstants, build_dirs.srcdir, issfile)

    iscc_cmd.append(issfile)
    print 'Generating executable with command: %s' % ' '.join(iscc_cmd)
    subprocess.call(iscc_cmd)
    print '-- End of operations'
