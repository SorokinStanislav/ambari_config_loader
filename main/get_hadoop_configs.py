import traceback

from Ambari import Ambari
from download_configs import download
from mover import move_to, flush
from unarchivator import extract
import sys

# HDFS must be the last
configs = ['YARN', 'MAPREDUCE2', 'TEZ', 'HIVE', 'HDFS']


def run():
    target_dir = sys.argv[1]
    ambari_url = sys.argv[2]
    ambari_admin_login = sys.argv[3]
    ambari_admin_password = sys.argv[4]
    cluster_name = sys.argv[5]
    ambari = Ambari(ambari_url, ambari_admin_login, ambari_admin_password, cluster_name)

    for config in configs:
        try:
            file = download(config, ambari)
            extract(file)
            move_to(target_dir)
        except:
            print("Error occurred. Loading of " + config + " is skipped.")
            traceback.print_exc()
        print('------------------------ \n')

    flush()


# just run it
run()
