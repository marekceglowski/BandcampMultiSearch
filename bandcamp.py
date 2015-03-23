from bs4 import BeautifulSoup
import urllib.request
import codecs

list1 = []
list2 = []
final = []

print('Bandcamp Unofficial Multi Genre/Tag Compare')
print('-------------------------------------------')
str1 = input('Enter first genre/tag: ')
str2 = input('Enter second genre/tag: ')
str3 = input('Sort by popularity (1) or newness (2): ')
while ((str3 != '1') and (str3 != '2')):
    print('\tInvalid input! Please enter 1 or 2.')
    str3 = input('Sort by popularity (1) or newness (2): ')
popdate = 'pop' if (str3 == '1') else 'date'
print('Tags to be matched: \''+str(str1)+'\' and \''+str(str2)+'\'.')

print('Collecting data for first tag...')
for page in range(1,11):
    print('\tPage: '+str(page)+'/10');
    response = urllib.request.urlopen(
        'http://bandcamp.com/tag/'+str(str1)+'?page='+str(page)+'&sort_field='+popdate)
    html_doc = response.read()

    soup = BeautifulSoup(html_doc)

    for item in soup.find_all("li", class_="item"):
        insert = []
        insert.append(item.find('a').get('href'))
        insert.append(item.find('div', class_='itemtext').text)
        insert.append(item.find('div', class_='itemsubtext').text)
        insert.append(item.find('img').get('src'))
        list1.append(insert)

print('Collecting data for second tag...')
for page in range(1,11):
    print('\tPage: '+str(page)+'/10');
    response = urllib.request.urlopen(
        'http://bandcamp.com/tag/'+str(str2)+'?page='+str(page)+'&sort_field='+popdate)
    html_doc = response.read()

    soup = BeautifulSoup(html_doc)

    for item in soup.find_all("li", class_="item"):
        insert = []
        insert.append(item.find('a').get('href'))
        insert.append(item.find('div', class_='itemtext').text)
        insert.append(item.find('div', class_='itemsubtext').text)
        insert.append(item.find('img').get('src'))
        list2.append(insert)

print('Creating list intersection...')
for item1 in list1:
    if item1 in list2:
        final.append(item1)

print('Writing to HTML file...')
f = codecs.open(str(str1)+'+'+str(str2)+'.html','w','utf-8')
message = '<HTML><HEAD></HEAD><BODY>'
message += '<TABLE width="100%" border="0" cellspacing="0" cellpadding="0" align="center">'

count = 0
for i in final:
    if (count == 0):
        message += '<TR>'
    message += '<TD><IMG SRC="'+str(i[3])+'"><BR>'
    message += '<A HREF="'+str(i[0])+'">'
    message += str(i[1])+'<BR>'+str(i[2])
    message += '</A></TD>'
    count += 1
    if (count > 4):
        message += '</TR>'
        count = 0

if (message[-5:] != '</TR>'):
    message += '</TR>'

message += '</TABLE></BODY></HTML>'
f.write(message)
f.close()
print('Done! See '+str(str1)+'+'+str(str2)+'.html file for results.')
