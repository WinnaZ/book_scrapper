# -*- coding=utf-8 -*-
# import libraries
from __future__ import print_function
try:
    import urllib.request as urllib_request
except ImportError:
    import urllib2 as urllib_request

from bs4 import BeautifulSoup
from builtins import input

book = ""

#asks for the url of the book
quote_page = input("Insert the URL on the fisrt page, example:'http://fullbooks.net/a-court-of-mist-and-fury/page-1-1076467.html': \n")

#parses the url to get information out
url = urllib_request.urlparse(quote_page)
data = url.path.split("/")

#get the book name out of data
name_of_book = data[1]

#gets the important numbers of the url
info = (data[2].replace(".html","")).split("-")

hash_number = int(info[2]) -1
page_1 = int(info[1])

total_pages = int(input("Insert the total of pages:"))

print("Downloading {}".format((name_of_book.replace("-"," ")).title()))

for n in range(page_1, total_pages+1):
    hash_number= hash_number + 1
    
    quote_page = url.scheme + "://" + url.netloc + "/" + name_of_book + "/page-" + str(n) + "-" + str(hash_number) +".html"  


    hdr = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'User-Agent':'Mozilla/5.0'
        }

    # query the website and return the html to the variable page
    req = urllib_request.Request(quote_page, headers=hdr)
    page = urllib_request.urlopen(req)
 
    # parse the html using beautiful soup and store in variable soup
    soup = BeautifulSoup(page, 'html.parser')
 
    # Take out the <div> of name and get its value
    name_box = soup.find('div', attrs={'class': "chapter-content-p"})

    clean_text = name_box.text.strip() # strip() is used to remove starting and trailing
    print(type(clean_text))
    
    #apends page into .txt file
    file = open('books/'+name_of_book+'.txt', 'a')
    # clean_text = clean_text.encode('utf-8')
    file.write(clean_text)
    file.close
    
    print("Page...... {}".format(n)) 
print("Done! file saved as {}.txt".format(name_of_book))


