#!/usr/bin/python3
"""
Write a Fabric script that generates a .tgz archive
from the contents of the web_static folder
"""


from fabric.api import run
from fabric.api import local
from fabric.api import get
from fabric.api import put
from fabric.api import env
from datetime import datetime
import os

env.hosts = ['34.74.161.43', '35.185.60.222']


def do_pack():
    """ do_pack """
    complete_time = datetime.now()
    string_time = complete_time.strftime("%Y%m%d%H%M%S")
    tgz_name = string_time + '.tgz'
    local("mkdir -p versions")
    local("tar -cvzf versions/web_static_{} web_static".format(tgz_name))
    path_tgz = 'versions/web_static_{}'.format(tgz_name)
    if os.path.exists(path_tgz):
        return path_tgz
    else:
        return None


def do_deploy(archive_path):
    """ do_deploy """
    if os.path.exists(archive_path) is False:
        return False
    try:
        put(archive_path, "/tmp/")
        ar_path_no_ext = archive_patch.split('.')[0]
        ar_path_no_ext = archive_patch.split('/')[-1]
        run("mkdir -p /data/web_static/releases/{}".format(ar_path_no_ext))
        ar_tmp = '/tmp/{}.tgz'.format(ar_path_no_ext)
        run("tar -xvzf {} -C /data/web_static/releases/{}"
            .format(ar_tmp, ar_path_no_ext))
        run("rm {}".format(ar_tmp))
        run("mv /data/web_static/releases/web_static_{}/\
            web_static/* /data/web_static/releases/web_static_{}/"
            .format(ar_path_no_ext, ar_path_no_ext))
        run("rm -rf /data/web_static/current")
        run("ln -sf /data/web_static/releases/{} /data/web_static/current"
            .format(ar_path_no_ext))
        run("rm -rf /data/web_static/releases/web_static_{}/web_static"
            .format(ar_path_no_ext))
        return True
    except Exception:
        return False
