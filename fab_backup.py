
from fabric.api import *

import os
import time


__all__ = ['backup_db', ]


def mysqldump(db):
    date = time.strftime('%Y%m%d')
    dump_file = '/tmp/%(database)s-%(date)s.sql' % {'database': db['name'],
                                                    'date': date}
    db['dump_file'] = dump_file

    local('mysqldump --no-create-db --opt '
          '--user=%(user)s --password=%(password)s '
          '--host=%(host)s %(name)s > %(dump_file)s' % db)

    return dump_file


def psqldump(db):
    pass


def mongodbdump(db):
    pass


db_engine_dict = {'mysql': mysqldump,
                  'postgresql': psqldump,
                  'mongodb': mongodbdump}


def make_local_dumps():
    dump_file_list = []

    for db in env.backup_db_list:
        dump_function = db_engine_dict[db['engine']]
        dump_file = dump_function(db)
        dump_file_list.append(dump_file)

    return dump_file_list


def mount_remote_store():
    mount_point = env.backup_remote_store['mount_point']
    if not os.path.exists(mount_point):
        local('mkdir -p %s' % mount_point)

    local("echo '%(password)s' | "
          "sshfs -o port=%(port)s %(user)s@%(host)s:/%(path)s %(mount_point)s"
          " -o password_stdin" % env.backup_remote_store)

    return mount_point


def umount_remote_store():
    local("fusermount -u %s" % env.backup_remote_store['mount_point'])


def copy_dumps_to_remote_store(dump_file_list):
    remote_store_path = mount_remote_store()
    date = time.strftime('%Y%m%d')
    remote_dump_path = os.path.join(remote_store_path,
                                    env.backup_remote_store['sub_path_db'],
                                    date)

    if not os.path.exists(remote_dump_path):
        local('mkdir -p %s' % remote_dump_path)

    for dump_file in dump_file_list:
        basename_dump_file = os.path.basename(dump_file)
        remote_dump_file = os.path.join(remote_dump_path, basename_dump_file)
        local("cp %s %s" % (dump_file, remote_dump_file))

    umount_remote_store()


def backup_db():
    dump_file_list = make_local_dumps()
    copy_dumps_to_remote_store(dump_file_list)
