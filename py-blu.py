import os
import urllib2

url = "http://hosts-file.net"
hosts_lists = ["ad_servers", "emd", "exp", "fsa", "grm", "hjk", "mmt", "psh"]
local_hosts_files = "/var/opt/blu"
new_hosts = bool(0)

if not os.path.exists(local_hosts_files):
    os.makedirs(local_hosts_files)
    
for i in hosts_lists:
   #name of hosts list file
    target_file_name = i + ".txt"
    #full path to taget file
    local_file_path = local_hosts_files + '/' + target_file_name   
    
    with open(local_file_path,  'r') as f:
        line = f.readline()
        local_file_date = line.strip('#')
        f.close()
  
    #get remote header
    response =  urllib2.request.urlopen(url)
    httpheaders = response.info()
       
    #up to date?
    if not httpheaders['date'] in local_file_date:
        #delete old file
        os.remove(local_file_path)
        #open file to append
        local_file = open(local_file_path,  'a')
        #date stamp
        local_file.write("#" + httpheaders['date'] + "#")
        #wrtie to file
        local_file.write(response.read())
        #close file
        local_file.close()
        
        #set new hosts to trigger dnsmasq restart at end of script
        new_hosts = bool(1)
           
    
    
    

        

        
