# -*- coding: utf-8 -*-
import urllib2
import json
access_token ="2.00Hk5I5B3mz1gE5d178ada323SS3HB"  # 输入Token，类似2.00Hk5I5B3mz1gE5d178ada323SS3HB
with open('./ids.csv') as f:
    content=f.read()
##print content
ids=content.split('\n')[:-1]
url0="https://api.weibo.com/2/tags/tags_batch.json?access_token="+access_token+"&uids="
def count_tags(uids,tags):
    url=url0+'%2C'.join(uids)
    html=urllib2.urlopen(url).read()
    users_tags=json.loads(html)
    for user in users_tags:
        tags0=user['tags']
        for i in tags0:
            for j in i:
                if j!="weight":
                    tags[i[j]]=tags.get(i[j],0)+1
tags={}
n=0
while n<len(ids):
    count_tags(ids[n:n+20],tags)
    n=n+20
tags_text=['%s,%s'% (k,v) for k,v in tags.items()]
with open('../tags.csv','w') as f:
    f.write('\n'.join(tags_text).encode('gbk','ignore')) 
