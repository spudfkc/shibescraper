import urllib2
import pickle
from bs4 import BeautifulSoup

imgSuffixes = ["jpg", "jpeg", "png", "gif"]
sites = [
    'http://reddit.com/r/supershibe',
    'http://reddit.com/r/shibe',
    'http://reddit.com/r/doge'
]

def parseImgLinks(soup, links):
    for link in soup.find_all('a'):
        l = link.get('class')
        if not l is None and 'title' in l:
            if any(s in link.get('href') for s in imgSuffixes):
                links.append(link)


allLinks = []
for site in sites:
    soup = BeautifulSoup(urllib2.urlopen(site).read())
    parseImgLinks(soup, allLinks)

allLinks = set(allLinks)

f = open('links.html', 'w')

for l in allLinks:
    f.write(str(l) + '<br/>')
    src = l.get('href')
    f.write('<img src="' + str(src) + '"/><br/><br/>')
f.close()

print 'done.'

