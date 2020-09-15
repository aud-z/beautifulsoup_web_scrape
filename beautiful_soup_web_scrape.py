# BeautifulSoup web scrapping

from urllib.request import urlopen
from bs4 import BeautifulSoup

html=urlopen('http://www.treasury.gov/resource-center/'
             'data-chart-center/interest-rates/Pages/'
             'TextView.aspx?data=yieldYear&year=2019')

bsyc=BeautifulSoup(html.read(), "lxml")

fout=open('bysc_temp.txt', 'wt', encoding='utf-8')

fout.write(str(bsyc))

fout.close()


# print(str(bsyc.table))
# not the table we want and too long 

# get a list of all tables

table_list=bsyc.findAll('table')

# how many tables are there?
print('there are,', len(table_list), 'table tags')

# look at first 50 chars of each table
for t in table_list:
    print(str(t)[:50])

# only one class='t-chart' table, so add that
# to findAll as a dictionary attribute
tc_table_list=bsyc.findAll('table',
                           {"class": "t-chart"})

#how many are there?
print(len(tc_table_list), 't-chart tables')

# only 1 t-chart table, so grab it
tc_table=tc_table_list[0]
'''
# what are this table's components/children?
# each row is a child of the table
for c in tc_table.children:
    print(str(c)[:50])
'''

'''
# tag tr means table row, containing table data
# what are the children of these rwos?
for c in tc_table.children:
    for r in c.children:
        print(str(r)[:50])
'''

# we found the table data
# just get the contents of each cell
for c in tc_table.children:
    for r in c.children: # children of children of table
        print(r.contents)

# convert into dataframe
table_raw=[]
for c in tc_table.children:
    for r in c.children:
        table_raw.append(r.contents)

tot=len(table_raw)
count=0
for i in table_raw:
    if str(i[0]).contains('/19'):
        count+=1

obs=tot/(count+1)
print('the number of observations per row is: ', obs)

table_list=[]


for i in range(0, 40, 13):
    row=[]
    for cell in range(i, i+13):
        row.append(str(table_raw[cell][0]))
    table_list.append(row)

# check output
print(len(table_list)==len(table_raw)/obs

exit()
