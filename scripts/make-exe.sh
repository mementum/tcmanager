#! /bin/sh
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
# Spec file generated with
# pyinstaller --specpath=./scripts --onefile --windowed --noupx src/tcmanager.pyw
prevdir=`pwd`

basedir="$( cd "$( dirname "$0" )" && pwd )"
cd ${basedir}
cd ..

# Remove unneeded files (everything will be recompiled)
find . -name '*~' -exec rm -f {} \;
find . -name '*.bak' -exec rm -f {} \;
find . -name '*.pyc' -exec rm -f {} \;
find . -name '*.pyo' -exec rm -f {} \;

# Clean up previous builds
rm -rf build dist

# Build the executable
pyinstaller ./scripts/tcmanager.spec

cd ${prevdir}
