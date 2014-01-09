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
# Sample file to be edited
# TODO:
# -- Add bit that finds in which directory the script is (regardless of how it was called)
# -- Update the pyinstaller commands to the latest version

find . -name '*~' -exec rm -f {} \;
find . -name '*.pyc' -exec rm -f {} \;
find . -name '*.pyo' -exec rm -f {} \;

rm -rf bin

mkdir -p bin/pkg
cp scripts/make-exe.spec bin/pkg

python -OO ../pyinstaller/Build.py -y bin/pkg/vcexportmanager.spec
mv -f logdict* bin/pkg

cp LICENSE README bin/pkg/dist/vcexportmanager

