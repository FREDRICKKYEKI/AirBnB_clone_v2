#!/usr/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py) that distributes
an archive to your web servers, using the function do_deploy
"""
from fabric.api import put, run, env
from os.path import exists


env.hosts = ['35.153.17.172', '	100.25.155.61']
env.user = "ubuntu"


def do_deploy(archive_path: str):
    """ distributes an archive to your web servers"""

    if (exists(archive_path)) is False:
        print(f"{archive_path} doesn't exist")
        return False
    try:
        filename = archive_path.split("/")[-1]
        w_out_ext = filename.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, "/tmp/")
        run('mkdir -p {}{}/'.format(path, w_out_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(filename, path, w_out_ext))
        run('rm /tmp/{}'.format(filename))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, w_out_ext))
        run('rm -rf {}{}/web_static'.format(path, w_out_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, w_out_ext))

    except Exception as e:
        return False
