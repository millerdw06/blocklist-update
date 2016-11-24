#!/usr/bin/env python

import os
import requests

source_url = 'http://hosts-file.net'
hosts_lists = ['ad_servers', 'emd', 'exp', 'fsa', 'grm', 'hjk', 'mmt', 'psh']
cache_dir = '/var/opt/blu'

if not os.path.exists(cache_dir):
    os.makedirs(cache_dir)

for i in hosts_lists:
    filename = i +'.txt'
    cached_file = cache_dir + '/' + filename
    source_file = source_url + '/' + filename

    #get cached ETag
    if os.path.isfile(cached_file):
        f = open(cached_file, 'r')
        l = f.readline()
        cached_ETag = l.strip('\n')
        f.close()

    else:
        cached_ETag = '#NO_CACHED_FILE#'

    #get remote header
    req_head = requests.head(source_file)
    source_ETag = req_head.headers['ETag']
    req_head.close()

    #up to date?
    if cached_ETag != source_ETag :

        f = open(cached_file, 'w')
        r = requests.get(source_file)
        f.write(source_ETag + '\n')
        f.write(r.text)
        f.close()

