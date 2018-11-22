import urllib.request as urllib2

from Credentials import Credentials


class Ambari:

    def __init__(self, url, login, password, cluster):
        parsed_ambari_url = urllib2.urlparse(url)
        if parsed_ambari_url.scheme == '':
            self.scheme = 'http'
            self.host_and_port = parsed_ambari_url.path
        else:
            self.scheme = parsed_ambari_url.scheme
            self.host_and_port = parsed_ambari_url.netloc

        self.credentials = Credentials(login, password)
        self.cluster = cluster
