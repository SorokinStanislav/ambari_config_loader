from download_configs import download
from mover import move, flush
from unarchivator import extract

# HDFS must be the last
configs = ['YARN', 'MAPREDUCE2', 'TEZ', 'HIVE', 'HDFS']


def run():
    for config in configs:
        try:
            file = download(config)
            extract(file)
            move()
        except:
            print("Error occurred. Loading of " + config + " is skipped.")
        print('------------------------ \n')

    flush()


# just run it
run()
