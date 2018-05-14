# import libraries
from urllib2 import urlopen, Request , urlparse
from bs4 import BeautifulSoup
from urlparse import urlparse

book = ""

#asks for the url of the book
quote_page = raw_input("Insert the URL on the fisrt page, example:'http://fullbooks.net/a-court-of-mist-and-fury/page-1-1076467.html': \n")

#parses the url to get information out
url = urlparse(quote_page)
data = url.path.split("/")

#get the book name out of data
name_of_book = data[1]

#gets the important numbers of the url
info = (data[2].replace(".html","")).split("-")

hash_number = int(info[2]) -1
page_1 = int(info[1])

total_pages = int(raw_input("Insert the total of pages:"))

print "Downloading " + (name_of_book.replace("-"," ")).title()

for n in range(page_1, total_pages+1):
    hash_number= hash_number + 1
    
    quote_page = url.scheme + "://" + url.netloc + "/" + name_of_book + "/page-" + str(n) + "-" + str(hash_number) +".html"  


    hdr = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'User-Agent':'Mozilla/5.0'
        }

    # query the website and return the html to the variable page
    req = Request(quote_page, headers=hdr)
    page = urlopen(req)
 
    # parse the html using beautiful soup and store in variable soup
    soup = BeautifulSoup(page, 'html.parser')
 
    # Take out the <div> of name and get its value
    name_box = soup.find('div', attrs={'class': "chapter-content-p"})

    clean_text = name_box.text.strip() # strip() is used to remove starting and trailing
    
    #apends page into .txt file
    file = open('books/'+name_of_book+'.txt', 'a')
    clean_text = clean_text.encode('utf-8')
    file.write(clean_text)
    file.close
    
    print "Page......", n 
print "Done! file saved as", name_of_book+'.txt'


