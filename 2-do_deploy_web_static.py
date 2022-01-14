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
from os.path import exists

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
    """distributes an archive to the web servers"""
    if exists(archive_path) is False:
        return False

    try:
        file_tgz = file_n = archive_path.split("/")[-1]
        f_no_ext = file_tgz.split(".")[0]
        dir_tmp = "/tmp/{}".format(file_tgz)
        dir_rel = "/data/web_static/releases/"
        rel_noext = dir_rel + f_no_ext
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(dir_rel, f_no_ext))
        run('tar -xzf {} -C {}{}/'.format(dir_tmp, dir_rel, f_no_ext))
        run('rm {}'.format(dir_tmp))
        run('mv {}/web_static/* {}/'.format(rel_noext))
        run('rm -rf {}{}/web_static'.format(dir_rel, f_no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(dir_rel, f_no_ext))
        return True
    except Exception:
        return False
