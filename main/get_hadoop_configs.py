from Credentials import Credentials
from download_configs import download
from mover import move_to, flush
from unarchivator import extract
import sys

# HDFS must be the last
configs = ['YARN', 'MAPREDUCE2', 'TEZ', 'HIVE', 'HDFS']


def run():
    target_dir = sys.argv[1]
    ambari_url = sys.argv[2]
    credentials = Credentials(sys.argv[3], sys.argv[4])

    for config in configs:
        try:
            file = download(config, ambari_url, credentials)
            extract(file)
            move_to(target_dir)
        except:
            print("Error occurred. Loading of " + config + " is skipped.")
        print('------------------------ \n')

    flush()


# just run it
run()
