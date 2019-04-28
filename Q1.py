import urllib.request
import re

import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import math

#author = "Ian+Goodfellow"
#author = "Ian"
author = input('Input Author:')
url_origin="https://arxiv.org/search/?query=" + author + "&searchtype=author&start="
page=0
url=url_origin+str(page)
content =urllib.request.urlopen(url)
html_str=content.read().decode('utf-8')

#pattern='title is-5 mathjax[\s\S]*?</p>'
#result = re.findall(pattern, html_str)

pattern_cnt='of [\S]*? results'
result_cnt=re.findall(pattern_cnt,html_str)
result_cnt_string=''.join(result_cnt)
result_cnt_string=result_cnt_string.replace(',','')
result_cnt_string=result_cnt_string.split("of ")[1].split(" results")[0].strip()
cnt=int(result_cnt_string)
cnt=math.ceil(cnt/50)
#print(cnt)
result_years=[ ]
pattern_years='announced</span>[\s\S]*?</p>'
k=0
while k<cnt:
        url=url_origin+str(page)
        content =urllib.request.urlopen(url)
        html_str=content.read().decode('utf-8')
        result_years=result_years+re.findall(pattern_years, html_str)
        k=k+1
        page=page+50

print("[ Author: " + author + " ]")
#for r in result:
#        title=r.split("title is-5 mathjax\">")[1].split("</p>")[0].strip()
#        print(title)
a=1
year_list=[ ]
#print(result_years)
for r in result_years:
        print("-----------------------")
        print(a)
        a=a+1
        years=r.split("announced</span")[1].split("</p>")[0].strip()
        year=years[-5:-1]
        print(year)
        j=0
        con=0
        while  j<len(year_list):
                if year==year_list[j][0]:
                        year_list[j][1]=year_list[j][1]+1
                        con=1
                        break
                j=j+1
        if con==0:
                year_list.append([year,1])

year_list.sort()
x=[ ]
y=[ ]
j=0
while  j<len(year_list):
        x.append(year_list[j][1])
        y.append(year_list[j][0])
        j=j+1
n = np.arange(len(x))
plt.bar(n, x)
plt.xticks(n+.5, y)
for a,b in zip(n,x):
        plt.text(a, b+0.05, '%.0f' % b, ha='center',va= 'bottom',fontsize=12)
plt.show()