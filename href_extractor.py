import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
from datetime import datetime
import re
import os

done = False

while done is False:
    now = datetime.now()
    print('It is currently ' + str(now) + '.')

    # Create our text file to hold our hrefs
    fileName = "hrefs - " + str(now) + ".txt"
    fileHandle = open(fileName, "a")

    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    url = input('Enter URL for our starting point: ')
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all anchor tags
    tags = soup('a')
    for tag in tags:
        print(tag.get('href', None))
        if tag is not None:
            fileHandle.write(tag.get('href', None) + "\n")
            
    fileHandle.close()
    
    newFileName = re.search(r"(?<=>).*(?=<)", str(soup('title')))[0] + " - " + fileName
    print("New name for hrefs file:", newFileName)
    os.rename(fileName, newFileName)
    
    userInput = input("Enter anything but 0 to get hrefs from another page. If you enter 0, we're done!: ")
    if userInput == '0':
        done = True
