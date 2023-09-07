#!/usr/bin/python3
"""Script that deploys a web application"""
import os
from fabric.api import run, put, env, sudo


# Define your server IPs here
env.hosts = ['54.236.232.78', '3.90.83.202']


def do_deploy(archive_path):
    """Distribute and deploy an archive to web servers"""

    if not os.path.exists(archive_path):
        return False

    try:
        # Extract the version from the archive filename
        filename = os.path.basename(archive_path)
        version = filename.split('.')[0]

        # Create the release directory
        run("mkdir -p /data/web_static/releases/{}".format(version))

        # Upload the archive to the server
        put(archive_path, "/tmp/")

        # Extract the contents of the archive
        run("tar -xzf /tmp/{} -C/data/web_static/releases/{}/"
            .format(filename, version))

        # Delete the archive from /tmp
        run("rm /tmp/{}".format(filename))

        # Move the contents to the web_static directory
        run("mv /data/web_static/releases/{}/web_static/* "
            "/data/web_static/releases/{}/".format(version, version))

        # Remove the empty web_static directory
        run("rm -rf /data/web_static/releases/{}/web_static".format(version))

        # Delete the old symbolic link
        sudo("rm -rf /data/web_static/current")

        # Create a new symbolic link
        sudo("ln -s /data/web_static/releases/{}//data/web_static/current"
             .format(version))

        print("New version deployed successfully!")
        return True

    except Exception as e:
        print("Deployment failed:", str(e))
        return False
