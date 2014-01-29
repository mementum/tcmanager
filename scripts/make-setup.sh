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

prevdir=`pwd`

basedir="$( cd "$( dirname "$0" )" && pwd )"
cd ${basedir}
cd ..

odir="build/innosetup"

rm -rf ${odir}
mkdir ${odir}
cp LICENSE ${odir}
cp README.md ${odir}
cp -r dist/* ${odir}

iscc scripts/innosetup.iss

cd ${prevdir}
