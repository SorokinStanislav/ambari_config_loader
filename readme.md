### Load configs from Ambari (Version 2.6.0.0)

##### run:

```
git clone https://github.com/SorokinStanislav/ambari_config_loader
cd ambari_config_loader/main
python3 get_hadoop_configs.py <target_dir> <ambari_url> <ambari_admin_login> <ambari_admin_password> <cluster_name>
```

##### params:
* target_dir - local directory path with '/' in the end where configs will be placed. 
* ambari_url - URL of Ambari in style <scheme>://<host>:<port> or just <host>:<port>
* ambari_admin_login - Ambari admin login
* ambari_admin_password - Ambari admin password
* cluster_name - Name of Hadoop cluster

##### result files in target folder:
* core-site.xml
* yarn-site.xml
* mapred-site.xml
* tez-site.xml
* hive-site.xml
* hdfs-site.xml
