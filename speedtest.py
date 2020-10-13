#!/usr/bin/python

//must have MySQLdb installed and python3
import time, os, fnmatch, MySQLdb as mdb, logging
from decimal import Decimal

#Database Settings Variables 
dbhost = 'localhost'
dbuser = 'username'
dbpass = 'securepassword'
dbname = 'Internet'
#create a database with table name speedtest, with columns, id (auto increment int), dateandtime (datetime), ping (double), download (double) upload (double)

try:
    a = os.popen("python3 /usr/local/bin/speedtest-cli --simple").read()
    #split the 3 line result (ping,down,up)
    lines = a.split('\n')
    print (a)
    ts = time.time()
    date = time.strftime('%Y-%m-%d %H:%M:%S')
    #if speedtest could not connect set the speeds to 0
    if "Cannot" in a:
        ping = 0
        download = 0
        upload = 0   
    else:
        print (lines)
        ping = lines[0][6:11]
        download = lines[1][10:14]
        upload = lines[2][8:12]        
   
    try:
        con = mdb.connect(dbhost, dbuser, dbpass, dbname);
        cur = con.cursor()                   
        cur.execute('INSERT INTO speedtest (dateandtime, ping, download, upload) VALUES(%s,%s,%s,%s)', (time.strftime("%Y-%m-%d %H:%M:%S"), ping, download, upload))
        con.commit()  
        con.close()
        print("Updated DB")
    except e:               
        print ('DB Connection Closed: %s' % e)
except Exception:        
    time.sleep(5)
     
