fab_backup
==========

fab functions for backups db and files to remote server



install
=======

aptitude install sshfs

pip install fab_backup


setup
=====

# Create fab_settings.py where add variables to enviropment
# see example in fab_settings.py.example

from fabric.api import *

# databases access list

env.backup_db_list = [{'engine': 'mysql',
                       'name': '',
                       'user': '',
                       'password': '',
                       'host': ''},
                      {'engine': 'postgresql',
                       'name': '',
                       'user': '',
                       'password': '',
                       'host': ''},
                      {'engine': 'mongodb',
                       'name': '',
                       'user': '',
                       'password': '',
                       'host': ''}]

# remote store access

env.backup_remote_store = {'user': '',
                           'password': '',
                           'host': '',
                           'port': '22',
                           'path': '',
                           'sub_path_db': '',
                           'sub_path_files': ''}

# add to your fabfile
import fab_settings
from fab_backup import *

usage
=====

fab backup_db
