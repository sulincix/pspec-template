#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get
#more information : https://gitlab.com/sulinos/inary/tree/master/inary/actionsapi
def setup():
#Configure parameters
    autotools.configure("--line \
                         --another-line \")

def build():
#make command
    autotools.make("build")

def install():
#make install command with parameter
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
#create symlink
    inarytools.dosym("/usr/bin/example", "/bin/example")
#remove file
    inarytools.remove("/bin/example")


