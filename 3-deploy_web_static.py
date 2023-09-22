#!/usr/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py) that distributes
an archive to your web servers, using the function do_deploy
"""
from fabric.api import put, run, env, local
from os.path import exists, isdir
from datetime import datetime


env.hosts = ['35.153.17.172', '	100.25.155.61']
env.user = "ubuntu"


def do_pack():
    """Function to generate tgz"""
    try:
        date_now = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(date_now)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        return None


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


def deploy():
    """creates and distributes an archive to the web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
