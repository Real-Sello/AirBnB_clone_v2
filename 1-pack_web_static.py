#!/usr/bin/python3
"""Script that compresses files into .tgz format"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """Generates a .tgz archive"""

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = "versions/web_static_{}.tgz".format(timestamp)

    try:
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(archive_name))
        return archive_name
    except Exception as e:
        print("Error:", str(e))
        return None


if __name__ == "__main__":
    result = do_pack()
    if result:
        print("Archive created:", result)
    else:
        print("Archive creation failed.")
