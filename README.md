fab_backup
==========

fab functions for backups db and files to remote server


install
=======

aptitude install sshfs

pip install fab_backup


setup
=====


Create fab_settings.py where add variables to enviropment
see example in fab_settings.py.example

add to your fabfile

    import fab_settings
    from fab_backup import *


usage
=====

fab backup_db


cron
====

    00 1    * * *   www-data cd /srv/www-data/project && source ~/.virtualenvs/project/bin/activate && fab backup_db
