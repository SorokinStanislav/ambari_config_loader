import tarfile


def extract(file):
    with tarfile.open(file) as f:
        f.extractall('extracted/')
    print(file + ' extracted')

