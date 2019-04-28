import urllib.request
import re
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

pattern_authors='authors">[\s\S]*?</p>'
result_authors=[ ]

k=0
while k<cnt:
        url=url_origin+str(page)
        content =urllib.request.urlopen(url)
        html_str=content.read().decode('utf-8')
        result_authors=result_authors+re.findall(pattern_authors, html_str)
        k=k+1
        page=page+50

print("[ Author: " + author + " ]")
#for r in result:
#        title=r.split("title is-5 mathjax\">")[1].split("</p>")[0].strip()
#        print(title)
a=1
author_list=[ ]
for r in result_authors:
        #print("-----------------------")
        #print(a)
        a=a+1
        #print(r)
        authors=r.split("authors\">")[1].split("</p>")[0].strip()
        authors=authors[40:]
        #<span class=\"search-hit\">Authors:</span>
        #print(authors)
        pattern_author='">[\s\S]*?</a>'
        result_author=re.findall(pattern_author, authors)
        #print(result_author)
        for i in result_author:
                co_author=i.split("\">")[1].split("</a>")[0].strip()
                #print(co_author)
                j=0
                con=0
                while  j<len(author_list):
                        if co_author==author_list[j][0]:
                                author_list[j][1]=author_list[j][1]+1
                                con=1
                                break
                        j=j+1
                if con==0:
                        author_list.append([co_author,1])

author_list.sort()    
j=0
while  j<len(author_list):
        str="%s: %s times" % (author_list[j][0],author_list[j][1])
        print(str)
        j=j+1        