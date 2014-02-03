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

clean_patterns = ['*~', '*.bak', '*.pyc', '*.pyo',]
pyinst_cmd = ['pyinstaller', '--noconfirm']
scriptpattern = '*.spec'

if __name__ == '__main__':
    print '**-- Beginning of operations'
    print '-- Cleaning up backups/compiled pythons'
    build_utils.delete_files(build_dirs.srcdir, clean_patterns)

    print '-- Removing (if needed) previous executable generation directories'
    build_utils.del_dir_if_exists(build_dirs.builddir)
    build_utils.del_dir_if_exists(build_dirs.distdir)

    print '-- Locating the specfile'
    specfile, specfiles = build_utils.locate_single_file(build_dirs.scriptdir, scriptpattern)
    if not specfile:
        print '-- ERROR: Found the following %s file(s): %s'  % (scriptpattern, specfiles)
        sys.exit(1)

    pyinst_cmd.append(specfile)
    print '-- Generating executable with command: %s' % ' '.join(pyinst_cmd)
    subprocess.call(pyinst_cmd)
    print '**-- End of operations'
