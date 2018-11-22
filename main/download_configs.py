import urllib.request as urllib2

user = 'admin'
password = 'admin'


def get_url(elem):
    return 'http://192.168.246.10:8080/api/v1/clusters/HDP/services/' + elem + \
           '/components/' + elem + '_CLIENT?format=client_config_tar'


def get_file_name(elem):
    return 'downloaded/' + elem + '.tar.gz'


def download(config):
    url = get_url(config)

    password_manager = urllib2.HTTPPasswordMgrWithPriorAuth()
    password_manager.add_password(None, url, user, password, is_authenticated=True)
    auth_manager = urllib2.HTTPBasicAuthHandler(password_manager)
    opener = urllib2.build_opener(auth_manager)

    file_name = get_file_name(config)
    f = open(file_name, 'wb')
    f.write(opener.open(url).read())
    f.close()
    print('Success load ' + config)
    return file_name




