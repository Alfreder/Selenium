from lxml import etree
import csv
#from scrapy.selector import Selector
import codecs
#import pymysql
import threading
import time
#html = codecs.open(r"write_data.html", "r", "utf-8")
html = codecs.open(r"write_data.html", "r", "utf-8")
content = html.read()
html.close()
#页面解析
page_source = etree.HTML(content)

d_1 = page_source.xpath("//td[contains(@id,'$cell$18')]/div/text()")
d_2 = page_source.xpath("//td[contains(@id,'$cell$19')]/div/text()")
d_3 = page_source.xpath("//td[contains(@id,'$cell$20')]/div/text()")
d_4 = page_source.xpath("//td[contains(@id,'$cell$22')]/div/text()")
d_5 = page_source.xpath("//td[contains(@id,'$cell$23')]/div/text()")
d_6 = page_source.xpath("//td[contains(@id,'$cell$24')]/div/text()")
d_7 = page_source.xpath("//td[contains(@id,'$cell$25')]/div/text()")
d_8 = page_source.xpath("//td[contains(@id,'$cell$26')]/div/text()")
d_9 = page_source.xpath("//td[contains(@id,'$cell$28')]/div/text()")
d_10 = page_source.xpath("//td[contains(@id,'$cell$29')]/div/text()")
"""print(d_1[0])
print(len(d_1))
print(d_2[0])
print(len(d_2))
print(d_3[0])
print(len(d_3))
print(d_4[0])
print(len(d_4))
print(d_5[0])
print(len(d_5))
print(d_6[0])
print(len(d_6))
print(d_7[0])
print(len(d_7))
print(d_8[0])
print(len(d_8))
print(d_9[0])
print(len(d_9))
print(d_10[0])
print(len(d_10))
#for i in range(0, len(d_2)):
#    print(d_2[i])
"""
for i in range(0,1000):
    d_1_list = []
    d_1_list.append(d_1[i])
    d_1_list.append(d_2[i])
    d_1_list.append(d_3[i])
    d_1_list.append(d_4[i])
    d_1_list.append(d_5[i])
    d_1_list.append(d_6[i])
    d_1_list.append(d_7[i])
    d_1_list.append(d_8[i])
    d_1_list.append(d_9[i])
    d_1_list.append(d_10[i])
    #print(d_1_list)
    data = d_1_list
    filename = r'data.txt'
    file = open(filename, 'a+',encoding='utf-8')
    for i in range(len(data)):
        s = str(data[i]).replace('[', '').replace(']', '')
        s = s.replace("'", '').replace(',', '') + ','
        file.write(s)
    file.write('\n')
    file.close()
print("保存文件成功")
