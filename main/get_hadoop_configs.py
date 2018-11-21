from download_configs import download
from mover import move, flush
from unarchivator import extract

# HDFS must be the last
configs = ['YARN', 'MAPREDUCE2', 'TEZ', 'HIVE', 'HDFS']


def run():
    for config in configs:
        file = download(config)
        extract(file)
        move()
        print('------------------------ \n')

    flush()

# just run it
run()

