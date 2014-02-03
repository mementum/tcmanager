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
import subprocess, sys
import build_dirs, build_utils

# pyinstaller does also generate the executable
# specs_cmd = ['pyinstaller', '--noconfirm', '--windowed', '--noupx']

# pyi-makespec does only generate the specfile
# --noconfirm is not accepted by pyi-makespec
specs_cmd = ['pyi-makespec', '--windowed', '--noupx', '--onefile']

# File(s) to look for when generating the spec file
scriptpattern = '*.pyw'

# onefile or onedir
appexetype='--onefile' # the other one being 'onedir'

if __name__ == '__main__':
    print '**-- Beginning of operations'

    print '-- Building spec generation command'
    specs_cmd.append('--specpath=' + build_dirs.scriptdir)
    specs_cmd.append('--additional-hooks-dir=' + build_dirs.hooksdir)
    specs_cmd.append(appexetype)

    pywfile, pywfiles = build_utils.locate_single_file(build_dirs.srcdir, scriptpattern)
    if not pywfile:
        print '-- ERROR: Found the following %s file(s): %s'  % (scriptpattern, pywfiles)
        sys.exit(1)
    
    specs_cmd.append(pywfile)

    print '-- Calling the following command:', ' '.join(specs_cmd)
    subprocess.call(specs_cmd)
    print '**-- End of operations'
