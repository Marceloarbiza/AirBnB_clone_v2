#!/usr/bin/python3
"""
Write a Fabric script that generates a .tgz archive
from the contents of the web_static folder
"""

from fabric.api import run
from fabric.api import local
from fabric.api import get
from fabric.api import put
from datetime import datetime
import os


def do_pack():
    """ do_pack """
    complete_time = datetime.now()
    string_time = complete_time.strftime("%Y%m%d%H%M%S")
    tgz_name = string_time + '.tgz'
    run("tar -cvzf tgz_name /data/web_static/")
    run("mkdir -p versions")
    if tgz_name in os.path:
        return tgz_name
    else:
        return None
