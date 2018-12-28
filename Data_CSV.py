from lxml import etree
import csv
import pandas as pd
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

d_1_list = []
d_1_list.append(d_1)
d_1_list.append(d_2)
d_1_list.append(d_3)
d_1_list.append(d_4)
d_1_list.append(d_5)
d_1_list.append(d_6)
d_1_list.append(d_7)
d_1_list.append(d_8)
d_1_list.append(d_9)
d_1_list.append(d_10)
print(d_1_list[9])

dataframe = pd.DataFrame({'a_name':d_1_list[0],'b_name':d_1_list[1],'c_name':d_1_list[2],'d_name':d_1_list[3],'e_name':d_1_list[4],'f_name':d_1_list[5],'g_name':d_1_list[6],'h_name':d_1_list[7],'i_name':d_1_list[8],'j_name':d_1_list[9]})
#dataframe = pd.DataFrame(d_1_list[0],d_1_list[1],d_1_list[2],d_1_list[3],d_1_list[4],d_1_list[5],d_1_list[6],d_1_list[7],d_1_list[8],d_1_list[9])

dataframe.to_csv("test.csv",index=False, mode='a',sep=',',encoding='utf_8_sig',header=0)
print("保存成功")



